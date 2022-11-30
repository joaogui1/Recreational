import qualified Data.Map as Map
import qualified Data.Char as Char
import qualified Control.Exception as Exception

import qualified Foreign.C.Types
import qualified System.Posix.IO as PosixIO

data E =
  -- literals
    EInt Int
  -- pure operators
  | EBinOp Op E E
  | ENot E
  -- global variables
  | EGet String
  | ESet String E
  -- control flow
  | EIf E E E
  | ESeq E E
  | EWhile E E
  | EDoWhile E E
  | ESkip
  -- I/O
  | EWriteByte E
  | EReadByte

data Op = Add | Sub | Eq | Lt | Lte | And  -- and many more

eval :: Map.Map String Int -> E -> IO (Int, Map.Map String Int)
eval vars (EInt i) = return (i, vars)
eval vars (EBinOp op e1 e2) = do
  (val1, vars') <- eval vars e1
  (val2, vars'') <- eval vars' e2
  return (evalOp op val1 val2, vars'')
eval vars (EGet var) = case Map.lookup var vars of
  Nothing -> error $ "no such variable: " ++ var
  Just x -> return (x, vars)
eval vars (ESet var e) = do
  (val, vars') <- eval vars e
  return (val, Map.insert var val vars)
eval vars (EWhile c e) = do
  (cond, vars') <- eval vars c
  case cond of
    0 -> return (0, vars')
    _ -> do
      (_, vars'') <- eval vars' e
      eval vars'' (EWhile c e) -- looping implemented with recursion
eval vars (EWriteByte byteE) = do
  (byte, vars') <- eval vars byteE
  if byte < 0 then error $ "Tried to print byte < 0: " ++ show byte
  else if 255 < byte then error $ "Tried to print byte > 255: " ++ show byte
  else PosixIO.fdWrite PosixIO.stdOutput [Char.chr byte]
  return (byte, vars')
eval vars (ENot e) = do
  (v, vars') <- eval vars e
  case v of
    0 -> return (1, vars)
    _ -> return (0, vars)
eval vars (EIf c t e) = do
  (cond, vars') <- eval vars c
  case cond of
    0 -> eval vars' e
    _ -> eval vars' t
eval vars (EDoWhile e c) = do
  (_, vars') <- eval vars e
  (cond, vars'') <- eval vars' c
  case cond of
    0 -> return (0, vars'')
    _ -> eval vars'' (EDoWhile e c)
eval vars (ESeq e1 e2) = do
  (_, vars') <- eval vars e1
  eval vars' e2
eval vars ESkip = return (0, vars)
eval vars EReadByte = do
  exp :: Either Exception.SomeException (String,Foreign.C.Types.CSize) <- Exception.try (PosixIO.fdRead PosixIO.stdInput 1)
  case exp of
    Left _ -> return (-1, vars)
    Right (str,count) -> do
      if count == 0 then
        return (-1, vars)
      else do
        let [c] = str
        return (Char.ord c, vars)


evalOp :: Op -> Int -> Int -> Int
evalOp Add a b = a + b
evalOp Sub a b = a - b
evalOp Eq a b = if a == b then 1 else 0
evalOp Lt a b = if a < b then 1 else 0
evalOp Lte a b = if a <= b then 1 else 0
evalOp And a b = if a == 0 || b == 0 then 0 else 1

writeTheAlphabet :: E
writeTheAlphabet =
  ESeq
    (ESet "x" (EInt 1))
    (EWhile (ENot (EBinOp Eq (EGet "x") (EInt 27))) (ESeq
      (EWriteByte (EBinOp Add (EInt 64) (EGet "x")))
      (ESet "x" (EBinOp Add (EGet "x") (EInt 1)))))

main :: IO ()
main = do
  eval Map.empty writeTheAlphabet
  return ()
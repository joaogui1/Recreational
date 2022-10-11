namespace BasicFunctions

#eval 2+2

def sampleFunction1 x := x*x + 3

def result1 := sampleFunction1 4573

#eval println! "The result of squaring the integer 4573 and adding 3 is {result1}"

def sampleFunction2 (x : Nat) := 2*x*x - x + 3

def result2 := sampleFunction2 (7 + 4)

#eval println! "The result of applying the 2nd sample function to (7 + 4) is {result2}"

def sampleFunction3 (x : Int) :=
  if x > 100 then
    2*x*x - x + 3
  else
    2*x*x + x - 37

#eval println! "The result of applying sampleFunction3 to 2 is {sampleFunction3 2}"

end BasicFunctions


def twice (f : Nat → Nat) (a : Nat) :=
  f (f a)

#eval twice (fun x => x + 2) 10

theorem twiceAdd2 (a : Nat) : twice (fun x => x + 2) a = a + 4 := rfl
-- The proof is by reflexivity. Lean "symbolically" reduces both sides of the equality
-- until they are identical.

#eval twice (· + 2) 10
-- `(· + 2)` is syntax sugar for `(fun x => x + 2)`.

-- The following command creates a new type `Weekday`.
inductive Weekday where
  | sunday    : Weekday
  | monday    : Weekday
  | tuesday   : Weekday
  | wednesday : Weekday
  | thursday  : Weekday
  | friday    : Weekday
  | saturday  : Weekday

#check Weekday.sunday

open Weekday
#check sunday
#check tuesday

def natOfWeekday (d : Weekday) : Nat :=
  match d with
  | sunday    => 1
  | monday    => 2
  | tuesday   => 3
  | wednesday => 4
  | thursday  => 5
  | friday    => 6
  | saturday  => 7

#eval natOfWeekday tuesday

def isMonday : Weekday → Bool :=
  -- `fun` + `match`  is a common idiom.
  -- The following expression is syntax sugar for
  -- `fun d => match d with | monday => true | _ => false`.
  fun
    | monday => true
    | _      => false

#eval isMonday monday
#eval isMonday sunday

-- Lean has support for type classes and polymorphic methods.
#eval toString 10
#eval toString (10, 20)

-- The method `toString` converts values of any type that implements
-- the class `ToString`.
-- You can implement instances of `ToString` for your own types.
instance : ToString Weekday where
  toString (d : Weekday) : String :=
    match d with
    | sunday    => "Sunday"
    | monday    => "Monday"
    | tuesday   => "Tuesday"
    | wednesday => "Wednesday"
    | thursday  => "Thursday"
    | friday    => "Friday"
    | saturday  => "Saturday"

#eval toString (sunday, 10)

def Weekday.next (d : Weekday) : Weekday :=
  match d with
  | sunday    => monday
  | monday    => tuesday
  | tuesday   => wednesday
  | wednesday => thursday
  | thursday  => friday
  | friday    => saturday
  | saturday  => sunday

#eval Weekday.next Weekday.wednesday
-- Since the `Weekday` namespace has already been opened, you can also write
#eval next wednesday

def Weekday.previous : Weekday -> Weekday
  | sunday    => saturday
  | monday    => sunday
  | tuesday   => monday
  | wednesday => tuesday
  | thursday  => wednesday
  | friday    => thursday
  | saturday  => friday

#eval next (previous wednesday)

-- We can prove that for any `Weekday` `d`, `next (previous d) = d`
theorem Weekday.nextOfPrevious (d : Weekday) : next (previous d) = d :=
  match d with
  | sunday    => rfl
  | monday    => rfl
  | tuesday   => rfl
  | wednesday => rfl
  | thursday  => rfl
  | friday    => rfl
  | saturday  => rfl

-- You can automate definitions such as `Weekday.nextOfPrevious`
-- using metaprogramming (or "tactics").
theorem Weekday.nextOfPrevious' (d : Weekday) : next (previous d) = d := by
  cases d       -- A proof by case distinction
  all_goals rfl  -- Each case is solved using `rfl`



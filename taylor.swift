import Glibc

//func taylor(x0: Double, order: Int, f: @differentiable (Double) -> Double) -> Double{
   // var ans = 0.0
   // var aux_f = f
  //  for i in 0..<order+1{
 //       ans += aux_f(x0)
//        (_, aux_f) = valueWithPullback(at: x0, in: aux_f)
//    }
//    return ans
//}

@differentiable(wrt: x)
func square(_ x: Double) -> Double {
    return x * x
}

let (value, deriv) =  valueWithPullback(at: 3, in: square)
let (_, snd) =  valueWithPullback(at: 3, in: deriv)
print(type(of: deriv))
print(type(of: square))
print(snd(1))
//print(taylor(x0: 0, order:0, f: square))

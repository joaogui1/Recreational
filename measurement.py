class Measurement:
    def __init__(self, x, delta_x):
        self.val = x
        self.delta = delta_x
    def __add__(self, o):
        ret = Measurement(self.val + o.val, self.delta + o.delta)
        return ret
    def  __sub__(self, o):
        ret = Measurement(self.val - o.val, self.delta + o.delta)
        return ret
    def __mul__(self, o):
        if(type(o) == type(self)):
            ret = Measurement(self.val * o.val, self.delta*o.val + self.val*o.delta)
        else:
            ret = Measurement(self.val*o, self.delta*o)
        return ret
    def __truediv__(self, o):
        ret = Measurement(self.val / o.val, (self.delta*o.val + self.val*o.delta)/(o.val**2))
        return ret
    def __pow__(self, n):
        ret = Measurement(self.val**n, (self.val**(n - 1))*n*self.delta)
        return ret
    def __str__(self):
        return f'{self.val} ± {self.delta}'

d = Measurement(9.7*(10**-4), 0.00005)
b = Measurement(0.02475, 0.00005)
d3 = d**3
w = Measurement(3.716, 9.81*10**(-5))
p = d3*b*(2.86)
E = w*4
E /= p
E *= 1/(10**10)


print(E)

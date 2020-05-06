from scipy.special import factorial
from numpy import exp
from math import pi, sqrt
import matplotlib.pyplot as plt

def grover_approx(n):
    ret = pow(n, n)/exp(n)
    ret *= sqrt(pi*(2*n + 1/3))
    return ret


def stirling_approx(n):
    ret = pow(n, n)/exp(n)
    ret *= sqrt(pi*(2*n))
    return ret

def exp_approx(n):
    ret = pow(n, n)/exp(n)
    return ret

def upper_bound(n):
    return pow(n, n)

def main():
    n = int(input())
    x = list(range(1, n + 1))
    grov_y = [factorial(i)/grover_approx(i) for i in range(1, n + 1)]
    stirling_y = [factorial(i)/stirling_approx(i) for i in range(1, n + 1)]
    exp_y = [factorial(i)/exp_approx(i) for i in range(1, n + 1)]
    upper_bound_y = [factorial(i)/upper_bound(i) for i in range(1, n + 1)]
    plt.plot(x, grov_y, 'r')
    plt.plot(x, stirling_y, 'b')
    plt.plot(x, exp_y, 'g')
    plt.plot(x, upper_bound_y, 'v')
    plt.show()

if __name__ == "__main__":
    main()

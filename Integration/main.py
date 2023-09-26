import numpy as np
from scipy.integrate import quad, dblquad

def polynomialFunction(x):
    return x**2 + 2*x + 1

def harmonicFunction(x,y):
    return x ** 3 - 3 * x * y ** 2

def logarithmPlusExponentialFunction(x):
    return np.log(x) + np.exp(x)

def analyticalSolutionPolynomial(a, b):


    F = lambda x: x**3/3 + x**2 + x

    return F(b) - F(a)

def analyticalSolutionHarmonic(a, b, c , d):



    F = lambda x,y:  (1/4) * (x**4 * y) - (1/2)* (x**2 * y**3)
    # + Const

    return F(b,d) - F(a,c)


def analyticalSolutionLogExp(a, b):

    F = lambda x: x*np.log(x) + np.exp(x) - x

    return F(b) - F(a)

def numericalIntegral(f, a, b):
    integral, error = quad(f, a, b)
    return integral

def main():
    a = float(input("Enter the start of the interval (for X): "))
    b = float(input("Enter the end of the interval (for X): "))
    c = float(input("Enter the start of the interval (for Y): "))
    d = float(input("Enter the end of the interval (for Y): "))
    print()


    integral_polynomial = numericalIntegral(polynomialFunction, a, b)
    integral_harmonic, error_harmonical = dblquad(harmonicFunction, a, b, c, d)
    integral_log_exp = numericalIntegral(logarithmPlusExponentialFunction, a, b)

    analytical_polynomial = analyticalSolutionPolynomial(a, b)
    analytical_harmonic = analyticalSolutionHarmonic(a, b,c,d)
    analytical_log_exp = analyticalSolutionLogExp(a, b)

    print("Integral of a polynomial (Numerical method):", integral_polynomial)
    print("Analytical solution of a polynomial:", analytical_polynomial)
    print("Polynomial error:", np.abs(integral_polynomial - analytical_polynomial))
    print()

    print("Integral of a harmonic function (numerical method):", integral_harmonic)
    print("Analytical solution of a harmonic function:", analytical_harmonic)
    print("Harmonic function error:", np.abs(integral_harmonic - analytical_harmonic))
    print()

    print("integral of logarithm/exponential (numerical method):", integral_log_exp)
    print("Analytical solution of logarithm/exponential:", analytical_log_exp)
    print("Logarithm/exponential error:", np.abs(integral_log_exp - analytical_log_exp))
    print()

main()

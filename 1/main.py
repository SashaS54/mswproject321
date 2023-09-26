import numpy as np
#
def func(x):
    return x**2

def numerical_derivative_adaptive_step(func, x,):
    epsilon=1e-6
    h = 1.0
    prev_derivative = None

    while True:
        h /= 2
        derivative = (func(x + h) - func(x - h)) / (2 * h)

        if prev_derivative is not None and abs(derivative - prev_derivative) < epsilon:
            break

        prev_derivative = derivative
    return derivative

def analytical_derivative(x):
    return 2 * x



def main():
    x = 2.0

    adaptive_derivative = numerical_derivative_adaptive_step(func, x)
    static_step_derivative = (func(x + 1e-5) - func(x - 1e-5)) / (2 * 1e-5)
    analytical_result = analytical_derivative(x)

    print("Analytical derivative:", analytical_result)
    print("Numerical derivative static step:", static_step_derivative)
    print("Numerical derivative adaptive step:", adaptive_derivative)


if __name__ == "__main__":
    main()

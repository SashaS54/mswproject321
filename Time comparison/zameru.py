import math
import random
import numpy as np
import time
#

def measureTime(func, *args):
    startTime = time.time()
    func(*args)
    endTime = time.time()
    return endTime - startTime


def printResults(CPythonTime, numpyTime):
    print(f"Time taken by CPython - {'{0:.10f}'.format(CPythonTime)} sec")
    print(f"Time taken by numpy - {'{0:.10f}'.format(numpyTime)} sec")


def sortArray(arr):
    arr.sort()


def sortArrayNumpy(arr):
    np.sort(arr)


def testArraySorting():
    print("Array sorting")

    arr1 = []
    arr2 = []
    for i in range(10000):
        num = random.randint(0, 100000)
        arr1.append(num)
        arr2.append(num)

    printResults(measureTime(sortArray, arr1), measureTime(sortArrayNumpy, np.array(arr2)))


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def factorialNumpy(x):
    math.factorial(x)


def testFactorialCalculation():
    print("\nFactorial calculation")

    x = 30

    printResults(measureTime(factorial, x), measureTime(factorialNumpy, x))


def generateRandomNumbers(n):
    for _ in range(n):
        random.random()


def generateRandomNumbersNumpy(n):
    np.random.rand(n)


def testRandomNumberGeneration():
    print("\nRandom number generation")

    n = 10000

    printResults(measureTime(generateRandomNumbers, n), measureTime(generateRandomNumbersNumpy, n))


def quadraticRoots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return
    sqrtDiscriminant = math.sqrt(discriminant)
    root1 = (-b + sqrtDiscriminant) / (2*a)
    root2 = (-b - sqrtDiscriminant) / (2*a)


def quadraticRootsNumpy(params):
    roots = np.roots(params)


def testQuadraticRootsCalculation():
    print("Quadratic roots calculation")

    a, b, c = 324923, 4239423, 435423

    printResults(measureTime(quadraticRoots, a, b, c), measureTime(quadraticRootsNumpy, np.array([a, b, c])))


def findMaxElem(arr):
    max(arr)


def findMaxElemNumpy(arr):
    np.max(arr)


def testFindingMaxElem():
    print("Finding max element in array")

    arr = [random.randint(0, 1000000) for _ in range(1000000)]

    printResults(measureTime(findMaxElem, arr), measureTime(findMaxElemNumpy, np.array(arr)))


def AllTest():
    testArraySorting()
    testFactorialCalculation()
    testRandomNumberGeneration()
    testQuadraticRootsCalculation()
    testFindingMaxElem()


if __name__ == "__main__":
    AllTest()

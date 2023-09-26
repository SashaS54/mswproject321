import random
import matplotlib.pyplot as plt

def simulateBasketShot(distance, shotsNum):
    successfulShots = 0
    successProbabilities = []

    for i in range(shotsNum):
        randomX = random.uniform(-distance, distance)
        randomY = random.uniform(0, distance)

        if randomY >= randomX**2:
            successfulShots += 1

        successProbabilities.append(successfulShots / (i + 1))

    successProbability = successfulShots / shotsNum
    print("The probability of success in shooting at the basket:", successProbability * 100, "%")

    plt.plot(range(1, shotsNum + 1), successProbabilities)
    plt.xlabel("The number of shots on goal.")
    plt.ylabel("Probability of success ")
    plt.title("The probability of success when shooting at the basket")
    plt.ylim(0, 1)
    plt.axhline(y=successProbability, color="r", linestyle="--", label="The average probability")
    plt.legend()
    plt.show()


    return successProbability


distance = 3
shotsNum = 100
successProbability = simulateBasketShot(distance, shotsNum)

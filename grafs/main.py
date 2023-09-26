import pandas as pd
import matplotlib.pyplot as plt
#
def Fix(x):
    if type(x) == str:
        x = x.replace(",", "")
        return x
    return 0

def main():
    csv1 = pd.read_csv("CSVs/1/russia_losses_personnel.csv")

    csv1["date"] = pd.to_datetime(csv1["date"])

    plt.figure(figsize=(16, 9))
    plt.plot(csv1["date"], csv1["personnel"], marker='o', linestyle='-')
    plt.title("Losts")
    plt.xlabel("Data")
    plt.ylabel("Quantity")
    plt.grid(True)
    plt.show()

    csv2 = pd.read_csv("CSVs/2/World_University_Rankings_2023.csv")

    csv2["No of student"] = csv2["No of student"].apply(Fix).astype(int)

    plt.figure(figsize=(16, 9))
    plt.plot(csv2["University Rank"], csv2["No of student"], marker='o', linestyle='-')
    plt.title("University Rank")
    plt.xlabel("Rang")
    plt.ylabel("Quantity")
    plt.grid(True)
    plt.show()

    csv3 = pd.read_csv("CSVs/3/diabetes.csv")

    plt.figure(figsize=(16, 9))
    plt.plot(csv3["Pregnancies"], csv3["Glucose"], marker='o', linestyle='-')
    plt.title("Diabetes stat")
    plt.xlabel("Pregnancies")
    plt.ylabel("Glucose")
    plt.grid(True)
    plt.show()

    csv4 = pd.read_csv("CSVs/4/Global Missing Migrants Dataset.csv")

    plt.figure(figsize=(16, 9))
    plt.plot(csv4["Incident year"], csv4["Number of Dead"], marker='o', linestyle='-')
    plt.title("Global Missing Migrants")
    plt.xlabel("Incident year")
    plt.ylabel("Number of Dead")
    plt.grid(True)
    plt.show()

    csv5 = pd.read_csv("CSVs/5/nuclear_power_plants.csv")

    csv5["ConstructionStartAt"] = pd.to_datetime(csv5["ConstructionStartAt"])
    csv5["OperationalFrom"] = pd.to_datetime(csv5["OperationalFrom"])

    plt.figure(figsize=(16, 9))
    plt.plot(csv5["ConstructionStartAt"], csv5["OperationalFrom"], marker='o', linestyle='-')
    plt.title("nuclear power plants")
    plt.xlabel("ConstructionStartAt")
    plt.ylabel("OperationalFrom")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

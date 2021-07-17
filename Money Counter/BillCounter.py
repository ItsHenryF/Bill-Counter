from numpy import NaN
import pandas as pd

def updateBills(valueToUpdate):
    numOfBills = int(input("Enter Number of {} Bills => ".format(valueToUpdate)))
    moneyValue = valueToUpdate
    while True:
        
        userChoice = input("Desposit => D\nWithdraw => W\n=>")
        if userChoice.upper() == 'D':
            df.loc[moneyDict[valueToUpdate], " Num of Bills"] = numOfBills + df[" Num of Bills"][moneyDict[valueToUpdate]]
            break
        elif userChoice.upper() == 'W':
            df.loc[moneyDict[valueToUpdate], " Num of Bills"] = df[" Num of Bills"][moneyDict[valueToUpdate]] - numOfBills
            break
        else:
            print("\n\nInvalid Option Entered\n\n")
    df.loc[moneyDict[valueToUpdate], "Total $"] = df[" Num of Bills"][moneyDict[valueToUpdate]] * int(valueToUpdate)
    return ""
validChoices = ["100", "50", "20", "10", "5", "1"]
def printMenu():
    print("Add Hundred Bills  => 100")
    print("Add Fifties Bills  => 50")
    print("Add Twenties Bills => 20")
    print("Add Tens Bills     => 10")
    print("Add Fives Bills    => 5")
    print("Add Ones Bills     => 1")
    print("Print Menu         => P")
    print("Exit Program       => Q")
    return ""
# Simplifies finding value in CSV File
moneyDict = {
    "100": 0,
    "50": 1,
    "20": 2,
    "10": 3,
    "5": 4,
    "1": 5
}
# Opens CSV 
df = pd.read_csv("MoneyTracker.csv")
# Adds up total to update total amount of money
totalMoney = 0
printMenu()
while True:
    userChoice = input("Enter Menu Option => ")
    if userChoice in validChoices:
        updateBills(userChoice)
        continue
    elif userChoice.upper() == "P":
        print("\n\n\n\n")
        printMenu()
        continue
    elif userChoice.upper() == "Q":
        print("\n\n\n\n")
        print("Updating Total and Exiting Program")
        for row in df["Total $"]:
            try:
                totalMoney = int(row) + totalMoney
            except:
                break
        break
    else:
        print("\n\n\nInvalid Option Selected.\n\n\n")
        printMenu()
# Updates Total Slot with Updated Balance of Bills
df.loc[7, "Total $"] = 0
df.loc[7, "Total $"] = totalMoney
# Saves and Updates MoneyTracker.csv
df.to_csv("MoneyTracker.csv", index=False)
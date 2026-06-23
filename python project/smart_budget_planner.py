print("Smart Travel Budget Planner")
budget = float(input("Enter Your complete Budget: "))

expence = {
    "Travel":0,
    "Food":0,
    "Accommodation":0,
    "Shopping":0
}

for i in expence:
    amount = float(input(f"Enter total amount spend on {i} : "))
    expence[i] += amount
    # print(expence[i])

total_spend = sum(expence.values())
print(total_spend)

with open("Summary.txt", "w") as file:
    file.write(f"Smart Travel Budget Planner \n")
    file.write(f"----------------------Expence Summary--------------------- \n")
    for j , k in expence.items():
        file.write(f"You spend {k} in {j} \n")

    file.write(f"----------------------------------------------------------\n")
    file.write(f"Total Spend is {total_spend}\n")
    file.write(f"Your Budget is {budget}\n")
    file.write(f"----------------------------------------------------------\n")

    if total_spend > budget:
        file.write("Your Budget is OUT")
    else:
        file.write("You are in budget ")
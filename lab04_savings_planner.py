# lab04_savings_planner.py

def get_non_negative(prompt):
    while True:
        value = float(input(prompt))
        if value >= 0:
            return value
        print("Please enter a non-negative number.")


def get_positive(prompt):
    while True:
        value = float(input(prompt))
        if value > 0:
            return value
        print("Please enter a number greater than zero.")


balance = get_non_negative("Starting balance: ")
deposit = get_positive("Monthly deposit: ")
rate = get_non_negative("Monthly interest rate (%): ")
goal = get_positive("Savings goal: ")

total_interest = 0
month = 0

print("\nMonth | Interest | New Balance")

while balance < goal and month < 60:
    month += 1
    interest = balance * rate / 100
    balance += interest
    total_interest += interest
    balance += deposit

    print(f"{month:5} | {interest:8.2f} | {balance:11.2f}")

    if balance >= goal:
        break

if balance >= goal:
    print(f"\nGoal reached in {month} months!")
else:
    print("\nGoal not reached within 60 months.")

print(f"Final balance: {balance:.2f}")
print(f"Total interest earned: {total_interest:.2f}")

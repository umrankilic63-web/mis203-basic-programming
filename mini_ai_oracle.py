
import random
import datetime
import time

# MINI AI ORACLE
# A mysterious digital fortune teller

answers = {
    "love": [
        "Someone may be hiding their true feelings.",
        "A meaningful connection takes time to grow.",
        "The past may teach you something about love.",
        "Do not confuse attention with affection."
    ],
    "future": [
        "An unexpected opportunity may change your plans.",
        "Your next chapter begins with a small decision.",
        "Something new is waiting beyond your comfort zone.",
        "Patience will reveal what haste cannot."
    ],
    "life": [
        "You already know more than you think.",
        "Not every ending is a failure.",
        "Your perspective may be the key to change.",
        "Sometimes the unknown is an invitation."
    ]
}

lucky_numbers = [3, 7, 11, 13, 21, 27, 33, 42, 77]

print("=" * 48)
print("             MINI AI ORACLE")
print("        Discover your hidden message")
print("=" * 48)

now = datetime.datetime.now()
print("Date:", now.strftime("%d/%m/%Y"))

name = input("\nWhat should the Oracle call you? ").strip()

if name == "":
    name = "Unknown Soul"

print("\nWelcome,", name + ".")
time.sleep(1)

while True:
    print("\nChoose your destiny:")
    print("1. Love")
    print("2. Future")
    print("3. Life")
    print("4. Reveal a secret number")
    print("5. Exit")

    choice = input("\nYour choice: ").strip()

    if choice == "5":
        print("\nThe Oracle whispers:")
        print("Your future is not written yet,", name + ".")
        print("You are the one who makes the choices.")
        break

    elif choice == "1":
        category = "love"
    elif choice == "2":
        category = "future"
    elif choice == "3":
        category = "life"

    elif choice == "4":
        print("\nThe Oracle has revealed your number:")
        print(random.choice(lucky_numbers))
        continue

    else:
        print("The Oracle does not understand your choice.")
        continue

    print("\nThe Oracle is reading your energy...")
    time.sleep(1)

    message = random.choice(answers[category])

    print("\n" + "-" * 48)
    print("A MESSAGE FOR", name.upper())
    print("Category:", category.upper())
    print(message)
    print("-" * 48)

    again = input("\nWould you like another message? (yes/no): ")
    if again.lower() == "no":
        print("Until we meet again, " + name + ".")
        break

print("\nThank you for visiting the Mini AI Oracle.")


import random
import time

print("Welcome to the Personality Test!")
print("Answer 4 questions to discover yourself!")

sunshine = 0
dreamer = 0
mystery = 0
thinker = 0

for i in range(4):
    print()
    print("Choose your favorite:")
    print("1. Friends and parties")
    print("2. Dreams and imagination")
    print("3. Mysteries and secrets")
    print("4. Books and learning")

    answer = input("Your answer (1-4): ")

    if answer == "1":
        sunshine = sunshine + 1
    elif answer == "2":
        dreamer = dreamer + 1
    elif answer == "3":
        mystery = mystery + 1
    elif answer == "4":
        thinker = thinker + 1
    else:
        print("Invalid answer!")

print()
print("Calculating your result...")
time.sleep(2)

if sunshine > dreamer and sunshine > mystery and sunshine > thinker:
    print("You are The Sunshine!")
    print("You are happy and energetic!")

elif dreamer > sunshine and dreamer > mystery and dreamer > thinker:
    print("You are The Dreamer!")
    print("You are creative and imaginative!")

elif mystery > sunshine and mystery > dreamer and mystery > thinker:
    print("You are The Mystery!")
    print("You are curious and love secrets!")

elif thinker > sunshine and thinker > dreamer and thinker > mystery:
    print("You are The Thinker!")
    print("You are calm and logical!")

else:
    print("You have a unique personality!")
    print("You are a mix of different personalities!")

print()
print("Thank you for playing!")

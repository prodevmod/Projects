import random

roll = random.randint(1,6)
print("🎲 You rolled : ", roll )

#Optional : Loop it

while input("Roll again? (y/n): ") == "y":
    roll = random.randint(1,6)
    print("🎲 You rolled : ", roll )

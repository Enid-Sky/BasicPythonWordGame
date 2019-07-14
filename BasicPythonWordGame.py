import time

print()
print("Welcome to the game Racer's Revenge")
time.sleep(2)
print("The game is about to start...")
time.sleep(1)
print("Booting up...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("Ready")
print()

# Get username
name = input("Hello, What's your name? ")
name = name.title()

# Intro

print()
print("Welcome to game,", name, "!")
print("Buckle and get ready for the race of a lifetime!")
print()

# Ask user if excited

excited = input("Are you excited to drive? Type Y or N? ")
excited = excited.upper()

if excited == "Y":
    print("Cool, I knew you'd say that!")

else:
    print("Well it's too late to back out now!")

# Getting Ready

print()
print("It's time to get ready for this game :)")

# Number of competitors

print("How many cars do you want to beat in this game?")

while True:
    num_cars = input("> ")
    num_cars = int(num_cars)

    if num_cars >= 10:
        break

    print("Aim for higher try again")


print("Now that's the spirit, you got this!")

# Little Helper

print()
print("You are allowed to bring one little companion to help you navigate the road.")

print("What kind of companion animal would you like to bring?")
companion_type = input("> ")
print("What is your companion's name?")
companion_name = input("> ")
companion_name = companion_name.title()

# Confirm animal navigator

print("That's awesome you want to have", companion_name, "the", companion_type)

# Car Decor

print()
print("We have awesome car selections for your choosing.")
print("Your options are:")
print(" A  Sleek, modern minimalism")
print(" B  Retro/vintage space age")
print(" C  SF Hippie chic")

print("Which car would you like to select? Choose A, B or C.")
car_choice = input("> ")
car_choice = car_choice.upper()

if car_choice == "A":
    car = "Modern Speedster"

elif car_choice == "B":
    car = "Retro Speedster"

elif car_choice == "C":
    car = "Hippie Speedster"

else:
    car = "Horse!"

print("Nice choice,", name, "and", companion_name, "!")
print("you will be cruising in your", car, "! Hope you win this race!")

# timer

timer = 5


while timer > 0:
    print(timer, "...")
    time.sleep(2)
    timer = timer - 1
print("Get set go!")

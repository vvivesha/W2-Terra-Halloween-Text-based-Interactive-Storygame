import turtle
import random
import time
#not sure why, but apparently I will need this next line of imported code stuff to make the slow-typing work out..? (Found through tutorial's comment section)
from time import sleep
print("    STARGAZERS")
time.sleep(0.5)
print("~~~~~~~~~~~~~~~~~")
print("--GAME SETTINGS--")
for gap in range(5):
    print(" ")


#best stars:
#ss_star = turtle.color("silver", "white") #silvy star
#goldie_star = turtle.color("white", "orange") #goldie star (aka goldfish)
#fiery_star = turtle.color("orange", "red") #blazey star (fiery)
#hard_star = turtle.color("gray", "black") #impeccable, impossible un-spottable star (aka game-changer star)
#seasonal stars:
#snow_star = turtle.color("silver", "white") #snowy star
#fall_star = turtle.color("yellow", "orange") #autumn star (maple leaf!)
#summer_star = turtle.color("brown", "red") #burning-hot summer star
#spring_star = turtle.color("brown", "yellow") #spring star!
#reg stars:
#yellow = turtle.color("yellow")
#silver = turtle.color("silver")
#blue = turtle.color("blue")
#purple = turtle.color("purple")
#red = turtle.color("red")
#orange = turtle.color("orange")
#green = turtle.color("green")
#white = turtle.color("white")
#turtle.forward(100)
#star_colors = [yellow, silver, blue, purple, red, orange, green, white]
#skip_settings = input("==>  Randomize game settings? This will skip the rest of the game-settings-questions.  (y/n)")
#if skip_settings == "y":
#    rc = random.choice
#   rc(star_colors)
 #   random.choice(star_location)
 #   random.choice(star_size)
 #   random.choice(star_quantity)
  #  random.choice(leaf_count)
  #  random.choice(leaf_size)
   # random.choice(leaf_location)
    #random.choice(leaf_penalizer_count)
    #random.choice()




dark_mode = input("-->  Activate dark mode?(y/n)  ")
if dark_mode == "y":
    #ANSI codes for terminal colors!
    print("\033[1;32;40m]")
    print("<Dark mode enabled>")
if dark_mode == "n":
    print("<Rad-dark-mode/old-school-terminal-mode was not enabled>")
    print(" :C  <-- Fred prefers dark mode")

#try to get stars from turtle to work...

print("/===============\ ")
seconds = 6
for countdown_3 in range(5):
    time.sleep(1)
    seconds -= 1
    print(str(seconds) + "...")
    print(" ")
time.sleep(1)
seconds -= 1
print(str(seconds) + "!!!")

#print("/--")
#print("Welcome, fellow Hack Clubber.")
#

#these were used to test if the commits were working :)
#print("thank you for helping me fix the issue!!")
#print("                                     --/")
#print("igone this; testing to see if commit button works and is out of rebase mode (vscode)")

name = input("And what would your name be?  ")
time.sleep(0.5)
print("/--")
print("Happy Halloween, " + name + ".")
print("                          --\ ")

for gap in range(3):
    print(" ")

time.sleep(2)
print("You are standing in front of your open closet.")
def slow_print(text, delay):
    for letter in text:
        print(letter, flush = True, end = "")
        sleep(delay)
slow_print("You have...  THREE costumes to choose from.", 0.1)
for gap in range(2):
    print(" ")
print("🦆 (duck)")
print("🐻 (bear)")
print("🧙 (mage)")
time.sleep(0.2)
costume = input("Would you like to be a duck, bear, or a mage?  ")

if costume == "duck":
    print("🦆 Quack! Now let\'s go outside to begin this spooky night.")
if costume == "bear":
    print("🐻 What an adorable bear costume!")
if costume == "mage":
    print("🧙 How magical!")

#variables:
weather_options = ["rainy", "stormy", "windy" ]
weather = random.choice(weather_options)
location = "home"
time_range = range(5, 400)

#storyline 1:
while location == "home":
    loop = "incomplete"
    print("Options: ")
    print("1-- look outside from your bedroom window")
    print("2-- find a candy bag")
    time.sleep(1)
    action = input("What will you do?")
#actions:
    if action == "1":
        print("Oh! It\'s quite " + weather + " outside.")
        time.sleep(0.5)
        print("You still need a candy bag!")
        time.sleep(0.2)
        input("<Press enter to go back>")
    if action == "2":
        candy_bag_options = ["a brown sock", "a pumpkin-shaped bucket", "a large pillowcase", "a plastic shopping bag"]
        candy_bag = random.choice(candy_bag_options)
        time_spent = random.choice(time_range)
        slow_print("You search for... " + str(time_spent) + " seconds, and find... " + candy_bag + ".", 0.05)
        print(" ")
        input("<Press enter to continue>")
        loop = "complete"
    if action not in ["1", "2", "One", "one", "Two", "two"]:
        print("Please choose what you will do next! (Type '1' or '2')")
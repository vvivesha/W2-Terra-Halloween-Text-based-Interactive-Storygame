print("hi")
import turtle
import random
import time
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
for countdown_3 in range(6):
    time.sleep(1)
    seconds -= 1
    print(seconds + "...")
    print(" ")
time.sleep(1)
seconds -= 1
print(seconds + "!!!")

print()
print("Welcome, fellow Hack Clubber.")
time.sleep(1)

print("/--")
print("thank you for helping me fix the issue!!")
print("                                     --/")
print("igone this; testing to see if commit button works and is out of rebase mode (vscode)")
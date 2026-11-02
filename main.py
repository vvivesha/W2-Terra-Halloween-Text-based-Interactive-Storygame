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

satisfied = "false"

while satisfied == "false":
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
    for gap in range(2):
        print(" ")
    time.sleep(0.2)
    costume = input("Would you like to be a duck, bear, or a mage?  ")

    if costume == "duck":
        satisfied = "true"
        print("🦆 Quack! Now let\'s go outside to begin this spooky night.")
        break
    if costume == "bear":
        satisfied = "true"
        print("🐻 What an adorable bear costume!")
        break
    if costume == "mage":
        satisfied = "true"
        print("🧙 How magical!")
        break
    else:
        satisfied = "false"
        for gap in range(2):
            print(" ")
        print("<Please wait until the typing animation has concluded before you start typing your request.")
        time.sleep(1)
        print("<Invalid costume option was requested. Please try again>")
        for gap in range(2):
            print(" ")

if satisfied == "true":
    for gap in range(3):
        print(" ")
    slow_print("⊹₊˚  <moving on to stage 1>", 0.08)
    print(" ")
    time.sleep(0.1)
for gap in range(3):
    print(" ")

#variables:
weather_options = ["rainy", "stormy", "windy" ]
weather = random.choice(weather_options)
stage = 1
time_range = range(5, 400)
node = "incomplete"
candy_bag_and_time_selected = "false"




#storyline 1:
while stage == 1:
    if node == "finished":
        time.sleep(0.2)
        print("You are able to continue to the next stage. You can still go back and explore the other options!")
        return_to_node = input("<Press enter when ready to move on. Or, type   Q   to go back.>")
        if return_to_node in ["Q", "q"]:
            node = "incomplete"
            if node == "incomplete":
                continue
        else:
            for gap in range(2):
                print(" ")
            print("─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧")
            print(name + " [to self] >>>  I\'m done here.")
            print("─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧")
            for gap in range(2):
                print(" ")
            node = "finished"
            break
    for gap in range(2):
        print(" ")
    slow_print('''You are in your bedroom. The time is 6 PM. 
    You have been grounded for the rest of the month... 
    but today is Halloween...
    the last day of of the month. 
    You are DETERMINED to sneak out tonight.''', 0.05)
    for gap in range(3):
        print(" ")
    print("Options: ")
    print("1-- look outside from your bedroom window")
    print("2-- find a candy bag")
    time.sleep(1)
    print(" ")
    action = input("What will you do?")
#actions:
    if action == "1":
        print("Oh! It\'s quite " + weather + " outside.")
        time.sleep(0.5)
        print("Get your candy bag!")
        time.sleep(0.2)
        input("<Press enter to go back>")
    if action == "2":
        while candy_bag_and_time_selected == "false":
            candy_bag_options = ["a brown sock", "a pumpkin-shaped bucket", "a large pillowcase", "a plastic shopping bag"]
            candy_bag_random = random.choice(candy_bag_options)
            time_spent_random = random.choice(time_range)
            candy_bag_and_time_selected = "true"
            slow_print("You search for... " + str(time_spent_random) + " seconds, and find... " + candy_bag_random + ".", 0.05)
            print(" ")
        if candy_bag_and_time_selected == "true":
            candy_bag = candy_bag_random
            time_spent = time_spent_random
            print("You have a candy bag!!")
            time.sleep(0.3)
        input("<Press enter to continue>")
        node = "finished"
        
    if action not in ["1", "2", "One", "one", "Two", "two"]:
        print("Please choose what you will do next! (Type '1' or '2')")
while node == "finished":
    for gap in range(2):
        print(" ")
    slow_print("⊹₊˚‧︵‿₊⊱·✶·⊰₊‿︵‧˚₊⊹  ", 0.03)
    slow_print("Time passes... <moving on to stage 2>", 0.01)
    slow_print("  ⊹₊˚‧︵‿₊⊱·✶·⊰₊‿︵‧˚₊⊹", 0.03)
    time.sleep(1)
    break
    skip_anim = input("<Press enter to skip the animation. Press Q to dismiss this message>")
    if skip_anim == "Q":
        stage == 2
        slow_print("⊹₊˚‧︵‿₊⊱·✶·⊰₊‿︵‧˚₊⊹  ", 0.03)
        print("Time passes... <moving on to stage 2>", 0.2)
        slow_print("  ⊹₊˚‧︵‿₊⊱·✶·⊰₊‿︵‧˚₊⊹", 0.03)
        break


#==========================================================================================
node = "finished"
stage = 2
#==========================================================================================
for gap in range(2):
    print(" ")
time.sleep(1.5)



#stage 2:
if stage == 2:
    while stage == 2:
        for gap in range(5):
            print(" ")
        if node == "finished":
            break
        if costume == "bear":
            stealth = 70
        if costume == "duck":
            stealth = 40
        if costume == "mage":
            stealth = 50
        slow_print("<The " + weather + " weather is over.>  Your mom has yet to come back from work, and your dad is raking up fallen leaves by himself, in the front yard.", 0.01)
        time.sleep(0.2)
        print("You want to sneak out to go trick-or-treating.")
        for gap in range(3):
            print(" ")
        time.sleep(0.2)
        print("Options:  ")
        print("1-- Leave through the window")
        print("2-- Do dad's yardwork for him and then sneak out")
        print("3-- Say you\'re going to drop off some textbooks at the local library")
        for gap in range(3):
            print(" ")
        action = input("What will you do?  ")
#options:
        if action == "1":
            for gap in range(2):
                print(" ")
            print("It\'s still " + weather + " outside.")
            if stealth <= 45:
                for gap in range(2):
                    print(" ")
                slow_print("Unfortunately, you are not stealthy enough to get past Dad.", 0.1)
                node = incomplete
                print("<Please pick another option>")
                continue
            if stealth >= 45:
                for gap in range(2):
                    print(" ")
                slow_print("You open the window and make quick work of exiting the house.", 0.1)
                print("Well done!")
                time.sleep(0.01)
                slow_print("And now, you're slinking through the backyard.")
                print("Lucky for you, there\'s one mighty-tall \'ol oak tree to shield you from Dad\'s view.")
                node = "finished"
                continue
        if action == "2":
            for gap in range(2):
                print(" ")
            print("─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧")
            print(name + " >>>  'Hey, Dad. I\'m sorry for cheating on my history test. Here, let me take care of that.'")
            print("Dad [in a rich, wise voice] >>>  'Oh, child. Thank you.'")
            print("─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧")
            for gap in range(2):
                print(" ")
            node = "finished"
            continue
        if action == "3":
            for gap in range(2):
                print(" ")
            print(" ")
            slow_print("You snatch a pen from your older sibling\'s desk, ")
            print(" ")
            time.sleep(0.1)
            print("─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧")
            print(name + " [writing a note] >>>  Dear parants: I am going to drop off a few school textbooks that are due at 7:30 PM today. I\'ll stay safe! Don\'t be mad, please.")
            print("─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧ ─── ✦ ─── ☾ ─── ✦ ─── ✧")
            time.sleep(0.1)
            print("You pin the note to the fridge using a magnet in the shape of a cartoon ghost.")
            node = "finished"
            continue
        

#moved from in between stage 1 and 2.
next_stage = "n"

        #map opportunity:
while node == "finished":
    if next_stage == "y":
        break
    time.sleep(1)
    map_view = input("Would you like to see a map of the property? (y/n)  ")
    for gap in range(3):
        print(" ")
    if map_view == "y":
        slow_print("         ===MAP OF YOUR HOUSE===", 0.01)
        print(" ")
        print('''    (Your room)         (Back yard)
               ______________________________________
              |        |          |                  |             |  |  
              |        |          |                  |             |  |
              |        |          |            |     |             |  |
              |_____   |          |            |     |             |  |    
              |                   |            |_   _|     <-- Front door
              |________________|      _________|                   |  |
                            |               |                      |  |
                            |               |                      |  |
                            |               |   <-- Garage         |  |
                            |_______________|                      |  |
                               (Front yard)                        |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                               (Sidewalk)                          |  |
___________________________________________________________________|  |
______________________________________________________________________|''')
        for gap in range(3):
            print(" ")
        next_stage = input("<Press enter to continue>")
        break
    if map_view == "n":
        slow_print("<You skipped viewing the map>", 0.02)
        print(" ")
        next_stage = input("<Press   Q   to continue to Stage 2>")
        if next_stage in ["Q", "q"]:
            next_stage = "yes"
            continue
        else:
            for gap in range(2):
                print(" ")
        time.sleep(0.2)
        print("<Please provide a valid input>")
        for gap in range(2):
            print(" ")
            continue

if next_stage in ["Q", "q"]:
            stage = 2
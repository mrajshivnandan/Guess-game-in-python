# stone paper scissor game
import random

no_of_dial = 1
print("You can play for 10 times if you score is more than computer you will win")
spc = {"s": "stone", "p": "paper", "c": "scissor"}
option = ["stone", "paper", "scissor"]
for key, value in spc.items():
    print(f"Type {key} for {value}")

dial= 10
computer_point= 0
human_point= 0


w= "You Won"
l= "You Loose"
while no_of_dial <= dial:

    guess_spc = (input())
    ran = random.choice(option)
    guess_spc= guess_spc.lower()
    try:
        if spc[guess_spc] == ran :
            print("tie 0 point to both")
            print("you selected ",spc[guess_spc],"and computer selected",ran)
            print(f"Your point is {human_point} and computer point is {computer_point}")
        elif spc[guess_spc] == "paper" and ran == "stone" :
            human_point = human_point + 1
            print("you selected ",spc[guess_spc],"and computer selected stone")
            print(f"Your point is {human_point} and computer point is {computer_point}")
            print(w)
        elif spc[guess_spc] == "paper" and ran == "scissor":
            computer_point = computer_point + 1
            print("you selected ",spc[guess_spc],"and computer selected scissor")
            print(f"Your point is {human_point} and computer point is {computer_point}")
            print(l)
        elif spc[guess_spc] == "stone" and ran == "scissor" :
            human_point = human_point + 1
            print("you selected ",spc[guess_spc],"and computer selected scissor")
            print(f"Your point is {human_point} and computer point is {computer_point}")
            print(w)
        elif spc[guess_spc] == "stone" and ran == "paper" :
            computer_point = computer_point + 1
            print("you selected ",spc[guess_spc],"and computer selected paper")
            print(f"Your point is {human_point} and computer point is {computer_point}")
            print(l)
        elif spc[guess_spc] == "scissor" and ran == "paper" :
            human_point = human_point + 1
            print("you selected ",spc[guess_spc],"and computer selected paper")
            print(f"Your point is {human_point} and computer point is {computer_point}")
            print(w)
        elif spc[guess_spc] == "scissor" and ran == "stone" :
            computer_point = computer_point + 1
            print("you selected ",spc[guess_spc],"and computer selected stone")
            print(f"Your point is {human_point} and computer point is {computer_point}")
            print(l)
    except Exception as e:
        print(e)
        print("Type only s, p, c don't try other")
        break
    print(dial - no_of_dial, "number of dial left")
    no_of_dial = no_of_dial + 1
    if no_of_dial> dial:
        if human_point> computer_point:
            print("You have won against computer by", human_point-computer_point, " points")
        if human_point< computer_point:
            print("You have lost against computer by",computer_point-human_point, " points")
        elif human_point== computer_point:
            print("The match has been drawn")
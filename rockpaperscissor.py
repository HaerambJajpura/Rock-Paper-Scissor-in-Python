
import random
def get_choice():
    player_choice=input("Enter your choice(rock, paper, scissor): ")
    options=["rock","paper","scissor"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    if player==computer:
        return "it's a tie!"
    elif player=="rock":
        if computer=="paper":
            return "paper grabs the rock you lose"
        if computer=="scissor":
            return "rock smashes the scissor you win"
    elif player=="paper":
        if computer=="scissor":  
            return "scissor cuts the paper you lose"
        if computer=="rock":
            return "paper grabs the rock you win"  
    elif player=="scissor":
        if computer=="paper":
            return "scissor cuts the paper you win"
        if computer=="rock":
            return "rock breaks the scissor you lose"


while True: 
    choices=get_choice()
    print(choices)
    if choices["player"] == "exit":
        break
    result=check_win(choices["player"],choices["computer"])
    print(result)
    print("-----------------------------------------------------------\n")
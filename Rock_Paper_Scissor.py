import random as r


#out comes are limited so it can be predefine
outcomes = {
    ("rock","paper"): "You lose",
    ("paper","scissor"): "You lose",
    ("scissor","rock"): "You lose",
    ("paper","rock"): "You Win",
    ("scissor","paper"): "You Win",
    ("rock","scissor"): "You Win"
}

#sets of choices so that computer can pick any of them randomly
actions = ["rock", "paper", "scissor"]

print("____________________________________Welcome to rock,paper and scissor game____________________________________")

#running the until user wants to quit
while True:
    computer_choice = r.choice(actions) #randomly selecting the action from above list

    # taking user input
    user = input("Enter the action for example, rock for rock, paper for paper, scissor for scissor or q for exiting the game: ").lower()

    #checking if user really enter a valid input
    if user not in ("rock","paper","scissor","q"):
        print("please enter a vaild action")
        continue
    #checking if user and computer made the same choices
    elif computer_choice == user:
        print("Draw")
    #checking if user wants to quit
    elif user == "q":
        print("Thank you for playing")
        break
    else:
        #selecting the out come on the basis of choice made by user and computer and printing them
        print("your action: ",user,",","computer's action: ",computer_choice)
        print(outcomes[(user,computer_choice)])

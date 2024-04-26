import random as r
chances = 5

# taking input from user 
def user_input(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("please enter a interger value like 1,2,3,5 etc")

def guessing(ran_num, maxrange, chance):
    while chances > 0: # check if chances are left
        user = user_input("Please guess a number: ") #taking the number from user that user gussed
        if user == ran_num: # if user hussed the number correctly
            print("you beat the game!!!")
            print("Thanks for playing")
            break
        # if user exceed the given range
        elif user > maxrange:
            print("please enter a number within range")
        else:
            # with wrong answer chance will be reduce till 0
            chance -= 1

            #checking if user gussed no. is too low or too high
            if user > ran_num:
                print("the number is too big")
            else:
                print("the number is too small")
            print("Chances left", chances) # remainding user of chances they have
    else:
        # if user has 0 chances then ending the game and declaring the answer
        print("Run out of chances")
        print("The number is", ran_num)
        print("Thanks for playing")

def play_game():
    # limiting the random value range for game
    max_range = user_input("please provide maximum range: ")
    random_num = r.randrange(0, max_range) # generating the random number
    guessing(random_num, max_range, chances)

def main():
    # asking user to want to play again or not if not then exiting the program
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()

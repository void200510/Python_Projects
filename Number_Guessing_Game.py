import random as r
chances = 5

print('''
Welcome to the Number Guessing Game!
Rules:
1. Enter an +ve integer value only.
2. Choose the maximum range (must be greater than 0).
3. The random number will be between 1 and your chosen maximum range.
4. Chances will not be deducted for out-of-range inputs.
5. You have a total of 5 chances to guess the number.
''')

# taking input from user 
def user_input(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("please enter a interger value like 1,2,3,5 etc")

def guessing(ran_num, maxrange, chance):
    while chance > 0: # check if chances are left
        user = user_input("Please guess a number: ") #taking the number from user that user gussed
        if user == ran_num: # if user hussed the number correctly
            print("🎉you beat the game!!!")
            print("Thanks for playing")
            break
        # if user exceed the given range
        elif user > maxrange or user < 0:
            print("⚠️please enter a number within range")
        else:
            # with wrong answer chance will be reduce till 0
            chance -= 1

            #checking if user gussed no. is too low or too high
            if user > ran_num:
                print("⚠️the number is too big")
            else:
                print("⚠️the number is too small")
            print("Chances left", chance) # remainding user of chances they have
    else:
        # if user has 0 chances then ending the game and declaring the answer
        print("Run out of chances")
        print(f"😔The number is{ran_num}")
        print("Thanks for playing")

def play_game():
    # limiting the random value range for game
    while True:
        max_range = user_input("please provide maximum range: ")
        
        if max_range <= 0:
            print("please enter a value which is greater than 0")
        else:
            break
    random_num = r.randint(1, max_range) # generating the random number
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

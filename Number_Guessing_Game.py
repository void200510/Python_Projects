import random as r
chances = 5

def user_input(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("please enter a interger value like 1,2,3,5 etc")

def guessing(ran_num, maxrange, chance):
    while chances > 0:
        user = user_input("Please guess a number: ")
        if user == ran_num:
            print("you beat the game!!!")
            print("Thanks for playing")
            break
        elif user > maxrange:
            print("please enter a number within range")
        else:
            chance -= 1
            if user > ran_num:
                print("the number is too big")
            else:
                print("the number is too small")
            print("Chances left", chances)
    else:
        print("Run out of chances")
        print("The number is", ran_num)
        print("Thanks for playing")

def play_game():
    max_range = user_input("please provide maximum range: ")
    random_num = r.randrange(0, max_range)
    guessing(random_num, max_range, chances)

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
#taking input from user and throwing error if user enter value other than int and continue to ask for correct input
def Input(message) -> int:
    while True:
        try:
            number = int(input(message + ": "))
            return number
        except ValueError:
            print("please enter a valid input for example numbers")
            continue

#calculate factorial through logic (5! = 5 * 4!)
def factorial(num) -> int:
    if num in (0,1):
        return 1
    else:
        return num * factorial(num - 1)

#staring point of program asking user to continue or quit and the number that it want get factorial of.
def starting():
    while True:
        user = input("Enter q for exiting the program or just simply press enter to continue the program: ").lower()
        if user == "q":
            print("Thank you for using it")
            break
        else:
            print(factorial(Input("Enter a number")))

if __name__ == "__main__":
    starting()

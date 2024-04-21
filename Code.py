from operator import index
import random as r
import string as s

code_store = []
encrypt = None

def output(list,string):
    string = ''.join(list) # converting list into string
    return print(string.lower())

#converting message to code
def coding(message):
    for i in message:
        code_store.append(i) #taking message and making list of it
    if len(message) > 3:
        code_store.append(code_store[0]) # add first letter to end and poping the first letter
        code_store.pop(0)
        c = 1
        while c <= 6:
            # add 3 letters at starting and ending of message
            random_letter = r.choice(s.ascii_letters)
            if c <= 3:
                code_store.append(random_letter)
            else:
                code_store.insert(0,random_letter)
            c += 1
    else:
        # if letters length is less than 3 it reverse it
        code_store.reverse()

    output(code_store, encrypt)

def decoding(code):
    for i in code:
        code_store.append(i) #taking code to convert it into message
    
    if len(code_store) < 3:
        code_store.reverse() # if letter is less than 3 it reverse it
    else:
        # it remove first and last three letters
        c = code_store[3:-3]
        #it add last letter to first position and then remove it
        c.insert(0,c[-1])
        c.pop(-1)
    output(c, encrypt)

def starting():
    while True:
        code_store.clear() #clear the list every time when process is complete
        user = input("enter 'c' for converting language in to code or 'd' for decoding a code or press 'q' to quit: ").lower()
        if user == 'c':
            coding(input("Enter a message: "))
        elif user == 'd':
            decoding(input("Enter a message: "))
        elif user == 'q':
            break
        else:
            print(print("Enter a valid value"))
            continue

if __name__ == "__main__":
    starting()
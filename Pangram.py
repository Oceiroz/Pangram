import string
def main():
    user_term = get_input("please enter a sentence and we will see if it is a pangram", str)
    pangram(user_term)

def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("this is not a valid input, please try again")
    return user_input

def pangram(user_term):
    alphabet = 0
    for char in string.ascii_lowercase:
        for letter in user_term:
            if char == letter:
                alphabet += 1
                break
            
    if alphabet == 26:
        print("your sentence IS a pangram")
    else:
        print("your sentence is NOT a pangram")

main()
def integer_input(prompt): 
    while True: 
        user_input = input(prompt) 
        try: 
            return int(user_input) 
        except ValueError: 
            print("Please only enter numbers: ") 

def addition():
    num1 = integer_input("Enter a number: ")
    num2 = integer_input("Enter another number: ")
    add = num1 + num2

    print(str(num1) + " plus " + str(num2) + " is " + str(add))

addition()
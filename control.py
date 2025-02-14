""" def login(password):
    #if statements evaluates to true we go to next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("what da password")
login("secret") """
""" 
def grade(score):
    if score >=92:
        print("A")
    elif score is >= 82
        print("B")
    elif score is >= 72
        print("C")
    else:
        print("F")

x = int(input("what da score"))
grade(x) """
""" 
def gamble(age, id):
    if age >= 21:
        if id == True:
            print("Gamble away")
        else:
            print("You need Id verification")
    else:
        print("you're too young") """

def gamble(age, id):
    if age >= 21 and id == True:
        print("have fun")
    elif age >= 21 and id == False:
        print("You need Id verification")
    else:
        print("you're too young")

""" raining = False        
if not raining == True:
        print("go for a walk")
if raining == False:
        print("go for a walk") """
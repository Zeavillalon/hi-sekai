#Pisay ASAP! 

#Dictionary/Database of usernames and passwords
users = {
    "Villalon, Zea" : "123"}

#List of snacks with their prices
snacks = {
    "Mamon":34,
    "Magic Flakes":25,
    "Lumpia":25,
    "Cream-O":10,
    "Skyflakes Condensada": 10,
    "Nissin Wafer": 5,
    "Fita":15,
    "Marie":15,
    "Casava Chips":50}

#User-defined Function for signing up
def signUp():
    print("""
==========SIGN-UP PAGE☆==========""")   
    while True:
        #Function that asks for the user to enter their full name for their username
        username = input("""
Please enter your full name (Last name, First Name): """).title()
    
        #checks if username exists in the database
        if username in users:
            print("Username already exists! Please try again.")
        
        else:
            #Asks for the user to create their password
            password = input("Create password: ")
            #Pairs value(password) to key(username)
            users[username] = password
            print("Account created succesfully!")
            break
           


#User-defined function for logging in
def login():
    print("""
==========LOG-IN PAGE☆==========
""")
    user = input("Please enter your full name (Last name, First Name), or enter 'exit': ").title()
    
    if user.lower() == "exit":
        print("Returning to welcome page...")
        return "exit"
    
    password = input("Enter your password: ")
    
    #checking for right username and password
    if user in users and users[user] == password:
        print("Log-in Successful!")
        return True
    else:
        print("Invalid username or password. Please try again.") 
        return False
    

#Main menu for login and sign-up
while True:
    print("""
================================""")
    print("""
Welcome to Pisay Asap☆! 

[1] Log-in (If you have an existing account in the application)
[2] Sign-up (If you plan to create an account in the application.)
[3] Close the program""")
    
    welcomeChoice = input("""
Choice(1, 2, or 3): """)

    #Condition to check if user chose to log-in or input 1
    if welcomeChoice == "1":
        result = login()
        
        if result == "exit":
            continue # Sends user back to the start of the while loop
        elif result == True:
            break # goes to snack menu
        else:
            continue # Sends user back to the start of the while loop
    
     #Condition to check if user chose to sign-up or input 2
    elif welcomeChoice == "2":
        signUp()
    
    
    elif welcomeChoice == "3":
        print("See you again! Speedy services only here at Pisay ASAP!")
        exit()
        
    else:
        print("Invalid Choice! Please try again.")
    
#Main menu/interface for ordering
        
print("""Welcome to the main menu!

================================

ORDER INFORMATION""")

while True:

    try:
         #Function to ask user's choice between snacks or meals 
        foodchoice = input("""
================================

Choose your food Category:

[1] Snacks
[2] Meals
[3] Exit the Program

Input your choice here: """)
        
        #Condition to check if user chose snacks or inputted 1.
        if foodchoice == "1":
            print("""
Choose from the provided list:
""")
            for food, price in snacks.items():
                print(f"""
{food}: Php {price}.00""")
            snackchoice = input("""
Pick your Snack: """)
            print("""
Feature NOT YET Available. Please Try again in the Future.""")
            continue
    
        #Condition to check if user chose meals or inputted 2.
        elif foodchoice == "2":
            
            print("""
Feature NOT YET Available. Please Try again in the Future.""")
            continue
        
        elif foodchoice == "3":
            print("See you again! Speedy services only here at Pisay ASAP!")
            break
        
    except ValueError:
        
        print("""
Invalid choice. Please Try Again.""")
        continue
    except TypeError:
        
        print("""
Invalid choice. Please Try Again.""")
        continue
    
        
        
            
        
        
        
            
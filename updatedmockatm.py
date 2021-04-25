# register
# firstname, lastname, password, email
# generates user account

# login
# - username or email and password

# bank operations

import random
import validation
import db
from getpass import getpass
from datetime import datetime 
now = datetime.now()
time = now.strftime("%X")
date = now.strftime("%d/%m/%y")

database = {} #dictionary

# initializing the system
def init():
    
    isValidOptionSelected = False
    print("********** WELCOME TO FASH BANK **********")
    
    while isValidOptionSelected == False:
        
        have_account = int(input("Do you have an account with us?\n 1 (Yes) \n 2 (No) \n"))
        
        if (have_account == 1):
            isValidOptionSelected = True
            login()
            
        elif (have_account == 2):
            isValidOptionSelected = True
            register()
            
        else:
            print("You have selected an invalid option\n")
            init()
    
    
def login():
    print("********** LOGIN TO YOUR ACCOUNT **********")
    account_number_from_user = input("What is your account number? \n")
    
    is_valid_account_number = validation.account_validation(account_number_from_user)
    
    if is_valid_account_number:
        
        password_from_user = input("What is your password?\n")
        
        user = db.user_authentication(account_number_from_user, password_from_user)
        
        if user:
            bank_operation(user)
            
       
        print('Invalid Account number password')
        login()
                    
    else:
       print("Invalid account number")
       init()
         
             

def register():
    
    print("*********** REGISTER **********")
    email = input("What is your email address?\n")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    password = input("What is your password?\n")
    account_number = generate_account_number()
    

    
   
    
    # database[account_number] = (first_name, last_name, email, password, 0)
    # database[8309798040] = ("fadeke", "fash", "f@gmail.com", "fara", 500)
    
    #using database module to create user record
    # prepared_user_details = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    is_database_created = db.create(account_number, first_name, last_name, email, password)
    
    if is_database_created:
        print(" Your account has been created succesfully")
        print(f"Your Account Number is {account_number}")
        login()
        
    else:
        print(" Something went wrong, please try again")
        register()
        
    
    
def bank_operation(user):
    print(f"********** Welcome to Fash Bank {user[0]} {user[1]} **********".upper())
    print("What bank operation would you like to perform?:\n")
    selected_option = int(input(" 1. Withdraw \n 2. Cash deposit \n 3. Check Balance \n 4. Transfer money \n 5. Complaint \n 6. Logout \n\n "))
                          
    if selected_option == 1:
        
        withdraw(user)
        
    elif selected_option == 2:
        
        deposit(user)
        
    elif selected_option == 3:
        
        balance(user)
        
    elif selected_option == 4:
        
        transfer(user)
        
    elif selected_option == 5:
        
        complaint()
        
    elif selected_option == 6:
        logout()
        
                 
def deposit(user):
    
    # action = 'deposit'
    acct_balance = user[4]
    print("\n********** DEPOSIT **********")
    deposit_amount = int(input("How much would you like to deposit? \n\n"))
    acct_balance = deposit_amount + int(acct_balance)
    print(f"\nYou have successfully deposited {deposit_amount} Naira")
    print(f"\nYour current account balance is  {acct_balance} Naira")
    # print("\nWould you like to perform another transaction?")
    
        
def withdraw(user):
    action = 'withdraw'
    acct_balance = user[4]
    try:
        withdrawal = float(input("How much would you like to withdraw?: "))
        if current_balance == 0 or withdrawal > current_balance:
            print("Insufficient funds")
            response = input("Would you like to make a deposit ? Type y for YES or n for NO: ".lower())
            if response == "y":
                deposit(user)
            elif response == "no":
                print("Thanks for banking with us")
                bankOperation(user)
        elif withdrawal <= 0:
            print(f"You cannot withdraw {withdrawal} from your account, try a higher value")
            withdrawal()
            
        else:
            current_balance = float(current_balance) - withdrawal
            print(f"you withdrew {withdrawal} and your available balance is : {current_balance}")
            user[4] = current_balance
    # withdrawal_amount = int(input("How much would you like to withdraw? \n\n"))
    # if withdrawal_amount <= acct_balance:  
    #     print("\nWithdrawal in Progress \n")
    #     print("Please take your cash")
    #     print("\nWould you like to perform another transaction?")
    # else:
    #     print("Insufficient funds, kindly try again")
            
    
def balance(user):
    acct_balance = user[4]
    
    balance = input("\nWould you like to check your balance? \n Select Y or N.\n")
    if (balance == "y" or balance == 'Y'):      
        print(f"Your current Account balance is {acct_balance}")
    #     print("\nYour account balance is %d Naira" %account_balance[userid])
    #     print("\nWould you like to perform another transaction?")
    # elif balance == "n" or balance == 'N':
    #     print("\nWould you like to perform another transaction?")
    # else:
    #     print("\nInput error, please try again")
    
    
# def transfer():
#     acct_balance = user[4]
#     action = 'transfer'
#     print("\nYou selected option %d \n" %selected_option)
#     transfer_amount = int(input("How much would you like to transfer from your account? \n"))
#     if (transfer_amount <= acct_balance[userid]):
#         print("Transaction in progress")
#         print("Transfer successful")
#     else:
#         print("Insufficient funds, kindly try again")
    
    
def complaint():
    print("Kindly input your complaint")
    complaint = input("\n What issue will you like to report \n")
    print("\nComplaint registered \n\nThank you for contacting us")
    


def generate_account_number():
     return random.randrange(1111111111, 9999999999)

    #  print("Generating Account Number...")
    #  generated_account_number = random.randrange(0000000000, 9999999999)
    #  print(f"Your Account Number is {generated_account_number}")
     
     
def logout():
    init()

        
    





#### ACTUAL BANKING SYSTEM ###
init()
print(database)

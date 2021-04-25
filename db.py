# create record
# read record
# update record
# delete record
# CRUD

#find user

import os
import validation

user_db_path = "data/user_record/"

def create(user_account_number, first_name, last_name, email, password):
    
    # create a file 
    # name of the file should be account_number.txt
    # add the user to the file
    # return true
    #if saving to file fails then delete create file
    
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    
    if does_acc_num_exist(user_account_number):
        
        return False
    
    if does_email_exist(email):
        
        print("Email already exists")
        return False
    
    completion_status = False
    
    try:
        
        f = open(user_db_path + str(user_account_number) + ".txt", "x" ) 
        
    except FileExistsError:
        does_file_have_data = read(user_db_path + str(user_account_number) + ".txt")
        
        if not does_file_have_data:
            delete(user_account_number)
        
        # delete the already created file, print out error then return false
        
        
    else:
        f.write(str(user_data));
        completion_status = True
        
    finally:   
        f.close();       
        return completion_status
    
    
def read(user_account_number):
    # find user with account number
    # fetch the content of the file
    
    is_valid_account_number = validation.account_validation(user_account_number)
    
    try:
        
        if is_valid_account_number:           
            
            f = open(user_db_path + str(user_account_number) + ".txt", "r" )
            
        else:
            
            f = open(user_db_path + user_account_number, "r")
    
    except FileNotFoundError:
        
        print(" User not found")
        
    except FileExistsError:
        
        print(" User does not exist")
        
    except TypeError:
        
        print(" Invalid account number format")
        
    else:
        
        return f.readline()
    
    return False

    
# def update(user_account_number):
    
#     # find user with account number
#     # fetch the content of the file
#     # update the content of the file
#     # save the file
#     # return true
#     first_name = read(user_account_number)[0]
#     last_name = read(user_account_number)[1]
#     email = read(user_account_number)[2]
#     password = read(user_account_number)[3]
#     acct_balance = read(user_account_number)[4]
    
#     if action == 'deposit':
#         acct_balance += deposit_amount
#         data = f"{first_name}, {last_name}, {email}, {password}, {acct_balance}"
#         f = open(user_db_path + str(user_account_number) + ".txt", "w" )
#         f.write(data)
        
#         print(f"Your current balance is {acct_balance}")
        
#         f.close()
        
#         return True
        
#     elif action == 'withdraw' or action == 'transfer':
#         acct_balance -= int(amount)
#         data = f"{first_name}, {last_name}, {email}, {password}, {acct_balance}"
#         f = open(user_db_path + str(user_account_number) + ".txt", "w" )
#         f.write(data)
        
#         print(f"Your current balance is {acct_balance}")
        
#         f.close()
    
def delete(user_account_number):
    
    # find user with account number
    # delete the user record (file)
    # return true

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:

            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful
            
    
def does_email_exist(email):

    all_users = os.listdir(user_db_path)
    
    for user in all_users:
        user_list = (str.split(read(user), ','))
        
        if email in user_list:
            return True
        
    return False


def does_acc_num_exist(user_account_number):
    
    all_users = os.listdir(user_db_path)
    
    for user in all_users:
        
        if user == str(user_account_number) + ".txt":
        
            return True
        
    return False    
    
    
def user_authentication(user_account_number, password):
    
    if does_acc_num_exist(user_account_number):
        
        user = (str.split(read(user_account_number), ','))
        
        if password == user[3]:
            return user
        
    return False
    
# def account_balance(user_account_number, acct_balance):
    
#     if does_acc_num_exist(user_account_number):
        
#         user = (str.split(read(user_account_number), ','))
        
#         if acct_balance == user[4]:
#             return user[4]
#     return False
        
        
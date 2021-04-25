def account_validation(account_number):
    
    if account_number:
             
            
        try:
            int(account_number)
                
            if len(str(account_number)) == 10:
                    
                return True
                
            else:
                    
                print("Account number must be 10 digits")
                return False
                
        except ValueError:
            # print("Invalid Account Number")
            return False
            
            
    else:
        print("Account number is a required field")
        return False

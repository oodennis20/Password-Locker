#! /usr/bin/env python3.6
import pyperclip
from accounts import User, Credential

def create_user(fstname,lstname,password):
    '''
    Function to create user account
    '''
    new_user = User(fstname,lstname,password)
    return new_user

def save_user(user):
    User.save_user(user)
    
def authenticate_user(firstname,password):
    '''
    To verify user is enabled
    '''
    confirm_user = Credential.confirm_user(first_name,password)
    return confirm_user

def create_credential(user_name,social_media,account_name,password):
    '''
    Creating new credentials
    '''
    new_credential = Credential(user_name,social_media,account_name,password)
    return new_credential

def save_credential(credential):
    Credential.save_credentials(credential)
    
def display_credentials(user_name):
    '''
    Display credentials saved by user
    '''
    return Credential.display_credentials(user_name)

def main():
    print('')
    print('Hello!! Welcome to Password Locker.')
    while True:
        print('')
        print("-",)
        print('Use these codes to navigate: \n ca-Create Account \n li-Log In \n ex-Exit')
        short_code = input('Please enter your choice ').lower().strip ()
        
        if short_code == 'ex':
            break
        
        elif short_code == 'ca':
            print("-",)
            print(' ')
            print('Create New Account: ')
            first_name = input ('Enter your First name- ').strip()
            last_name = input ('Enter your Last name- ').strip()
            password = input ('Enter your password- ').strip()
            save_user(create_user(first_name,last_name,password))
            print(" ")
            print(f'New Account Created for: {first_name} {last_name} using password: {password}')
        elif short_code == 'li': 
            
            print("-"*60) 
            print(' ')
            print('To login, enter your account details:')
            user_name = input('Enter your first name - ').strip()
            password = str(input('Enter your password - '))
            user_exists = authenticate_user(user_name,password)
            if user_exists == user_name:
                print(f'Welcome {user_name}. PLease choose an option to proceed.')
                print(' ')
                while True:
                    print("-",)
                    print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n ex-Exit')
                    short_code = input('Enter your choice: ').lower().strip()
                    print("-"*60)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Goodbye {user_name}')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Enter your credential details:')
                        
                        social_media = input('Enter the social media\'s name- ').strip()
                        
                        account_name = input('Enter your account\'s name - ').strip()
                        
                        while True:
                                print(' ')
                                print("-"*60)
                                print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                                pswd_choice = input('Enter an option: ').lower().strip()
                                
                                print("-"*60)
                                if pswd_choice == 'ep':
                                    print(" ")
                                    password = input('Enter your password: ').strip()
                                    
                                    break     
                                elif pswd_choice == 'gp':
                                    password = generate_password()
                                    
                                    break
                                elif pswd_choice == 'ex':
                                    break
                                else:
                                    print('Check! Wrong option entered. Try again.')        

                                    save_credential(create_credential(user_name,social_media,account_name,password))
                                    print(' ')
                                    print(f'Credential Created: Social Media: {social_media} - Account Name: {account_name} - Password: {password}')
                                    print(' ')
                    elif short_code == 'dc': 
                        print(' ')  
                        if display_credentials(user_name):
                            print('Nice! Here is a list of all your credentials')   
                            print(' ') 
                        else:
                            print(' ')       
                            print("Sorry, You don't have any credentials")
                            
                            print(' ')
                    else:
                        print(' ') 
                        print('Check! Wrong details entered. Please try again or Create an acoount')
                            
if __name__ == '__main__': 
    main() 

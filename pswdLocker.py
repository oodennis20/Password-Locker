#! /usr/bin/env python3.6
from accounts import User, Credential
import random
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
    confirm_user = Credential.confirm_user(firstname,password)
    return confirm_user

def generate_password(self):
    '''
    Function to automatically gen password
    '''
    pswd = [" cddjektygh", "fg2eefwder", "thgsmxeedtb"]
        
    print(random.choice(pswd))


def create_credential(user_name,social_media,account_name,password):
    '''
    Creating new credentials
    '''
    new_credential = Credential(user_name,social_media,account_name,password)
    return new_credential

def save_credential(credential):
    Credential.save_credentials(credential)
    
def display_credentials():
    '''
    Display credentials saved by user
    '''
    return Credential.display_credentials()
def credential_exists(social_media):
    return Credential.credential_exists(social_media)

def search_social_media(cls,social_media):
    return Credential.search_social_media(social_media) 

def search2_social_media(social_media):
    return Credential.search_social_media(social_media) 

def delete_credential(social_media):
    Credential.credentials_list.remove(social_media)
    
def main():
    print('')
    print('Hello!! Welcome to Password Locker.')
    while True:
        print('')
        print("$"*60)
        print('Use these codes to navigate: \n ca-Create Account \n li-Log In \n ex-Exit')
        short_code = input('Please enter an option ').lower().strip ()
        if short_code == 'ex':
            print('It was nice having you! Feel free to come back...')
            break
        
        elif short_code == 'ca':
            print("$"*60)
            print(' ')
            print('Create New Password locker Account: ')
            first_name = input ('Enter your First name- ').strip()
            last_name = input ('Enter your Last name- ').strip()
            password = input ('Enter your password- ').strip()
            save_user(create_user(first_name,last_name,password))
            print(" ")
            print(f'New Account Created for: {first_name} {last_name} using password: {password}')
        elif short_code == 'li': 
            print("$"*60) 
            print(' ')
            print('To login, enter your account details:')
            user_name = input('Enter your first name - ').strip()
            password = str(input('Enter your password - '))
            user_exists = authenticate_user(user_name,password)
            if user_exists == user_name:
                print(" ")
                print(f'Welcome {user_name}. Please choose an option to proceed.')
                print(' ')
                while True:
                    print("$"*60)
                    print('Navigation codes: \n cc-Create Social Media credentials \n dc-Display Credentials\n del-Delete Credential\n ex-Exit')
                    short_code = input('Choose an option: ').lower().strip()
                    print("$"*60)
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
                                print("$"*60)
                                print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password\n ex-exit')
                                pswd_options = input('Enter an option: ').lower().strip()
                                
                                print("$"*60)
                                if pswd_options == 'ep':
                                    print(" ")
                                    password = input('Enter your password: ').strip()
                                    save_credential(create_credential(user_name,social_media,account_name,password))
                                    print(" ")
                                    print(f'Credential Created: Social Media: {social_media} - Account Name: {account_name} - Password: {password}')
                                    
                                    break     
                                elif pswd_options == 'gp':
                                    pswd = "cddjektygh"
                                    print(random.choice(pswd))
                                    save_credential(create_credential(user_name,social_media,account_name,pswd))
                                    print("Great! Your password is generated successfully")
                                    print("$"*60)
                                    print(f'Credential Created: Social Media Name: {social_media} - Account Name: {account_name} - Password: {pswd}')
                                   
                                    
                                    break
                                elif pswd_options == 'ex':
                                    break
                                else:
                                    print('Sorry! Wrong option entered. Try again.')        

                                save_credential(create_credential(user_name,social_media,account_name,password))
                                print(f'Credential Created: Social Media Name: {social_media} - Account Name: {account_name} - Password: {password}')
                                print(' ')
                    elif short_code == 'dc': 
                        print(' ')  
                        if display_credentials():
                            print('Nice! Here is a list of all your credentials')   
                            print(' ') 
                            for credential in display_credentials():
                                print(f'Social Media Name: {credential.social_media} - Account Name: {credential.account_name} - Password: {credential.password}')
                                print(' ')
                        else:
                            print(' ')       
                            print("Sorry, You don't have any credentials")
                            
                            print(' ')
                    elif short_code == 'del':
                        print("App to delete")
                        yourname = input().lower()
                        
                        if credential_exists(yourname):
                            yournames = search2_social_media(yourname)
                            delete_credential(yournames)
                            print("Deleted succesfully")
                            
                        else:
                            print("Credential does not exist")
                            
                            
                            
                    else:
                        print(' ')
                        print('Sorry! Incorrect option entered. Try again.')
                else:
                    print(' ') 
                    print('Sorry! Wrong details entered. Please try again or Create an account')
            else:
                print("$"*60)
                print('Sorry! Wrong details entered. Please try again or Create an account')
                           
if __name__ == '__main__': 
    main() 

#! /usr/bin/env python3.6
import pyperclip
from accounts import User, Credential

def create_user(firstname,lstname,password):
    '''
    Function to create user account
    '''
    new_user = User(firstname,lstname,password)
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
    

if __name__ == '__main__': 
    main() 

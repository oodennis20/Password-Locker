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



if __name__ == '__main__': 
    main() 

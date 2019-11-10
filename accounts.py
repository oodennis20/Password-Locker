import pyperclip
import string
import random

class User:
    '''
    Class to create new user accounts and save them to help access the pswd locker
    '''
    
    users_list = []

    def __init__(self,first_name,last_name,password):

        '''
        Method to define the properties of the object
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    def save_user(self):
       User.users_list.append(self)
       
class Credential:
    '''
    Class that holds and saves user login details
    '''
    # class variables
    credentials_list = []
    # user_credentials_list = []
    
    @classmethod
    def confirm_user(cls,first_name,password):
        '''
        Method that checks if the name and password entered match entries in the user_list
        '''
        active_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                active_user = user.first_name
        return active_user
    
    def __init__(self,user_name,social_media,account_name,password):
            
        '''
        Method defining the properties each object will hold
        '''
        self.user_name = user_name
        self.social_media = social_media
        self.account_name = account_name
        self.password = password
        
    def save_credentials(self):
        Credential.credentials_list.append(self)
    
    def generate_password(self):
        '''
        Function to generate random passwords for social media accounts
        '''
        pswdchar = string.printable
        length = int(input('Enter password length desired: '))
        gen_pswd= ''
        for pswdchar in range(length):
            gen_pswd += random.choice(pswdchar)
        return gen_pswd
    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def search_social_media(cls,social_media):
        for credential in cls.credentials_list:
            if credential.social_media == social_media: 
                return credential
            
    @classmethod
    def copy_social_media(cls,social_media):
        find_credential = Credential.search_social_media(social_media)
        return pyperclip.copy(find_credential.password)
    @classmethod
    def copy_password(cls,social_media):
        '''
		Class method that copies a credential's password of a specific social media site after the credential's social media name is entered
		'''
        collect_pass = Credential.search_social_media(social_media)
        return pyperclip.copy(collect_pass.password)
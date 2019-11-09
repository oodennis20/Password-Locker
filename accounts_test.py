import unittest
import pyperclip
from accounts import User, Credential

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Function to help create user account before each test
        '''
        self.new_user = User("Clyde","Dennis","lit")
        
    def test_init_(self):
        self.assertEqual(self.new_user.first_name,"Clyde")
        self.assertEqual(self.new_user.last_name,"Dennis")
        self.assertEqual(self.new_user.password,"lit")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
    
        
class TestCredentials(unittest.TestCase):
    def test_confirm_user(self):
        self.new_user = User("Clyde","Dennis","lit")
        self.new_user.save_user()
        userZ= User("Clyde","Dennis","lit")   
        userZ.save_user()
        
        for user in User.users_list:
            if user.first_name == userZ.first_name and user.password == userZ.password:
                active_user = user.first_name
                return active_user
            
        self.assertEqual(active_user,Credential.confirm_user(userZ.password,userZ.first_name))
        
    def setUp(self):
        '''
        Function to create social media account credentials before each test
        '''
        self.new_credential = Credential("Clarke","Instagram","Kent","clarkekent")
        
    def test__init__(self):
        '''
        Confirm that credential creation is as expected
        '''
        self.assertEqual(self.new_credential.user_name,"Clarke")
        self.assertEqual(self.new_credential.social_media,"Instagram")
        self.assertEqual(self.new_credential.account_name,"Kent")
        self.assertEqual(self.new_credential.password,"clarkekent")
        
    def test_save_credentials(self):
        '''
        Confirm and test if the new credential info is being saved
        '''
        self.new_credential.save_credentials()
        snapchat = Credential("Clarke","snapchat","Kenty","clarkekenty")
        snapchat.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)
        
    def tearDown(self):
        User.users_list = []
        Credential.credentials_list = []
        
    def test_display_credentials(self):
        '''
        Confirm user can view correct credential details
        '''
        self.new_credential.save_credentials()          
        snapchat = Credential("Clarke","snapchat","Kenty","clarkekenty")
        snapchat.save_credentials()
        self.assertEqual(len(Credential.display_credentials(snapchat.user_name)),1)
        
    def test_search_social_media(self):
        '''
        confirm if the method returns correct social media credential
        '''
        self.new_credential.save_credentials()
        snapchat = Credential("Clarke","snapchat","Kenty","clarkekenty")
        snapchat.save_credentials()
        credential_exists = Credential.search_social_media("snapchat")
        self.assertEqual(credential_exists,snapchat)
    
    def test_copy_credential(self):
        '''
        Test to check if the copy credential copy will copy credential details correctly
        '''
        self.new_credential.save_credentials()
        snapchat =  Credential("Clarke","snapchat","Kenty","clarkekenty")
        snapchat.save_credentials()
        
        find_credential = None
        for credential in Credential.user_credentials_list:
            find_credential = Credential.search_social_media(credential.social_media)
            return pyperclip.copy(find_credential.password)
        credential.copy_credential(self.new_credential.social_media)
        self.assertEqual("clarkekenty",pyperclip.paste())
        print(pyperclip.paste())
        
        
        
if __name__ == '__main__':
    unittest.main()
        

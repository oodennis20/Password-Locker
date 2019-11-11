import unittest
from accounts import User, Credential

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Function to help create user account before each test
        '''
        self.new_user = User('Clyde','Dennis','lit')
        
    def test_init_(self):
        self.assertEqual(self.new_user.first_name,'Clyde')
        self.assertEqual(self.new_user.last_name,'Dennis')
        self.assertEqual(self.new_user.password,'lit')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
   
        
    
        
class TestCredentials(unittest.TestCase):
    def test_confirm_user(self):
        self.new_user = User('Clyde','Dennis','lit')
        self.new_user.save_user()
        userZ= User('Clyde','Dennis','lit')   
        userZ.save_user()
        active_user = Credential.confirm_user('Clyde','lit')
        self.assertTrue(active_user)
        
    def setUp(self):
        '''
        Function to create social media account credentials before each test
        '''
        self.new_credential = Credential('clarke','instagram','kent','clarkekent')
        
    def test__init__(self):
        '''
        Confirm that credential creation is as expected
        '''
        self.assertEqual(self.new_credential.user_name,'clarke')
        self.assertEqual(self.new_credential.social_media,'instagram')
        self.assertEqual(self.new_credential.account_name,'kent')
        self.assertEqual(self.new_credential.password,'clarkekent')
        
    def test_save_credentials(self):
        '''
        Confirm and test if the new credential info is being saved
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list),1)
        
    def tearDown(self):
        User.users_list = []
        Credential.credentials_list = []
        
    def test_display_credentials(self):
        '''
        Confirm user can view correct credential details
        '''
        self.new_credential.save_credentials()          
        instagram = Credential('clarke','instagram','kent','clarkekent')
        instagram.save_credentials()
        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)
        
    def test_delete_contact(self):
        Credential.credentials_list = []
    
    def test_search_social_media(self):
        '''
        Test to confirm if the method returns the correct social media credential
        '''
        self.new_credential.save_credentials()
        instagram = Credential('clarke','instagram','kent','clarkekent')
        instagram.save_credentials()

    def test_credential_exists(self):
        self.new_credential.save_credentials()          
        instagram = Credential('clarke','instagram','kent','clarkekent')
        instagram.save_credentials()
        
        credential_exists = Credential.credential_exists("instagram")
        self.assertTrue(credential_exists)
        
        
if __name__ == '__main__':
    unittest.main()
        

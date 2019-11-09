import unittest
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
        
    def tearDown(self):
        User.users_list = []
        
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
                
        
        
        
if __name__ == '__main__':
    unittest.main()
        

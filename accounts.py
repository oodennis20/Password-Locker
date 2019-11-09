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
    user_credentials_list = []
    
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
 

    

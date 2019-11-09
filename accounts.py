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
 

    

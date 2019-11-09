class User:
    '''
    Class to create new user accounts and save them to help access the pswd locker
    '''

    def _init_(self,first_name,last_name,password):

        '''
        Method to define the properties of the object
        '''
    
    def save_user(self):
       User.users_list.append(self)
 

    

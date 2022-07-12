from logger import log

class User:
    def __init__(self, user_id=None, username=None, password=None):
        self._user_id = user_id
        self._user_name = username
        self._password = password
    
    def __str__(self) -> str:
        return f'''
        User ID: {self._user_id},
        Username: {self._user_name},
        password: {self._password}
        '''
    
    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, new_id):
        self._user_id = new_id
        return self._user_id

    @property
    def username(self):
        return self._user_name
    
    @username.setter
    def name(self, name):
        self._user_name = name
        return self._user_name
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
        return self._password
    
  

if __name__ == '__main__':
    new_person = User(1, "Juanchito", "Ds@1257")
    log.debug(new_person)
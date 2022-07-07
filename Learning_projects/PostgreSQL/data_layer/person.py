from logger import log

class Person:
    def __init__(self, id=None, name=None, last_name=None, email=None):
        self._person_id = id
        self._name = name
        self._last_name = last_name
        self._email = email
    
    def __str__(self) -> str:
        return f'''
        Person ID: {self._person_id},
        Name: {self._name}, Last Name: {self._last_name},
        Email: {self._email}
        '''
    
    @property
    def person_id(self):
        return self._person_id
    
    @person_id.setter
    def person_id(self, id):
        self._person_id = id
        return self._person_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        return self._name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
        return self._email

if __name__ == '__main__':
    new_person = Person(1, "Juan", "Perez", "jperez@email.com")
    log.debug(new_person)
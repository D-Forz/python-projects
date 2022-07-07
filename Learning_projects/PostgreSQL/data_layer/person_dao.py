from connection import Connection
from person import Person
from logger import log
from pool_cursor import PoolCursor

class PersonDAO:
    '''
    DAO: (Data Access Object)
    CRUD: (Create - Read - Update - Delete)
    '''
    _SELECT     = 'SELECT * FROM person_db ORDER BY person_id'
    _INSERT     = 'INSERT INTO person_db(first_name, last_name, email) VALUES(%s, %s, %s)'
    _UPDATE     = 'UPDATE person_db SET first_name=%s, last_name=%s, email=%s WHERE person_id=%s'
    _DELETE     = 'DELETE FROM person_db WHERE person_id=%s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT)
            items = cursor.fetchall()
            persons = []
            for item in items:
                new_person = Person(item[0], item[1], item[2], item[3])
                persons.append(new_person)
            return persons
    
    @classmethod
    def insert(cls, new_person):
        with PoolCursor() as cursor:
            values = (new_person.name, new_person.last_name, new_person.email)
            cursor.execute(cls._INSERT, values)
            log.debug(f'New person added: {new_person}')
            return cursor.rowcount
    
    @classmethod
    def update(cls, person):
        with PoolCursor() as cursor:
            values = (person.name, person.last_name, person.email, person.person_id)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'Person updated: {person}')
            return cursor.rowcount
    
    @classmethod
    def delete(cls, person):
        with PoolCursor() as cursor:
            values = (person.person_id,)
            cursor.execute(cls._DELETE, values)
            log.debug(f'Object deleted: {person}')
            return cursor.rowcount

if __name__ == '__main__':  
    new_person = Person(name="Clara", last_name="Tellez", email="clarellez@email.pe")
    persons_inserted = PersonDAO.insert(new_person)
    log.debug(f'persons inserted: {persons_inserted}')

    # new_person = Person(1, "Juan Carlos", "Najera", email="juannajera@mail.co")
    # persons_updated = PersonDAO.update(new_person)
    # log.debug(f'persons updated: {persons_updated}')

    # new_person = Person(id=9)
    # persons_deleted = PersonDAO.delete(new_person)
    # log.debug(f'persons deleted: {persons_deleted}')

    persons = PersonDAO.select()
    for person in persons:
        log.debug(person)
    

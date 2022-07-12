from user import User
from logger import log
from pool_cursor import PoolCursor

class UserDAO:
    '''
    DAO: (Data Access Object)
    CRUD: (Create - Read - Update - Delete)
    '''
    _SELECT     = 'SELECT * FROM users ORDER BY user_id'
    _INSERT     = 'INSERT INTO users(username, password) VALUES(%s, %s)'
    _UPDATE     = 'UPDATE users SET username=%s, password=%s WHERE user_id=%s'
    _DELETE     = 'DELETE FROM users WHERE user_id=%s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT)
            items = cursor.fetchall()
            users = []
            for item in items:
                new_user = User(item[0], item[1], item[2])
                users.append(new_user)
            return users
    
    @classmethod
    def insert(cls, new_user):
        with PoolCursor() as cursor:
            values = (new_user.username, new_user.password)
            cursor.execute(cls._INSERT, values)
            log.debug(f'New User added: {new_user}')
            return cursor.rowcount
    
    @classmethod
    def update(cls, user):
        with PoolCursor() as cursor:
            values = (user.user_id, user.username, user.password)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'User updated: {user}')
            return cursor.rowcount
    
    @classmethod
    def delete(cls, user):
        with PoolCursor() as cursor:
            values = (user.user_id,)
            cursor.execute(cls._DELETE, values)
            log.debug(f'Object deleted: {user}')
            return cursor.rowcount

if __name__ == '__main__':  
    
    new_user = User(username="Clara", password="285")
    users_inserted = UserDAO.insert(new_user)
    log.debug(f'Users inserted: {users_inserted}')

    # new_user = User(1, "juan_c", "469")
    # users_updated = UserDAO.update(new_user)
    # log.debug(f'Users updated: {users_updated}')

    # new_user = User(id=9)
    # users_deleted = UserDAO.delete(new_user)
    # log.debug(f'Users deleted: {users_deleted}')

    persons = UserDAO.select()
    for person in persons:
        log.debug(person)
    

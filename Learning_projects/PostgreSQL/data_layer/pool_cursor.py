from logger import log
from connection import Connection

class PoolCursor:
    def __init__(self):
        self._connection = None
        self._cursor = None
    
    def __enter__(self):
        log.debug('Start method with __enter__')
        self._connection = Connection.create_connection()
        self._cursor = self._connection.cursor()
        return self._cursor
    
    def __exit__(self, exception_type, value_exception, traceback):
        log.debug('Finish method __exit__')
        if value_exception:
            self._connection.rollback()
            log.error(f"Rollback, an error has ocurred: {value_exception}: {exception_type} {traceback}")
        else:
            self._connection.commit()
            log.debug('commit of the transaction')
        self._cursor.close()
        Connection.release_connection(self._connection)

if __name__ == '__main__':
    with PoolCursor() as cursor:
        log.debug('inside with method')
        cursor.execute('SELECT * FROM person_db')
        log.debug(cursor.fetchall())
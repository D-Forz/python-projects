from logger import log
from psycopg2 import pool
import sys

class Connection:
    _DATABASE   = 'test_db'
    _USERNAME   = 'postgres'
    _PASSWORD   = 'admin'
    _DB_PORT    = '5432'
    _HOST       = '127.0.0.1'
    _MIN_CON    = 1
    _MAX_CON    = 5
    _pool       = None
    
    @classmethod
    def create_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    user        = cls._USERNAME,
                    password    = cls._PASSWORD,
                    host        = cls._HOST,
                    port        = cls._DB_PORT,
                    database    = cls._DATABASE
                )
                log.debug(f'Pool successfully created: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'An exception has ocurred in pool: {e}')
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def create_connection(cls):
        connection = cls.create_pool().getconn()
        log.debug(f'Connection from pool successfully created: {connection}')
        return connection

    @classmethod
    def release_connection(cls, connection):
        cls.create_pool().putconn(connection)
        log.debug(f'Connection returned to the pool: {connection}')

    @classmethod
    def close_connections(cls):
        cls.create_pool().closeall()

    
if __name__ == '__main__':
    connection_one = Connection.create_connection()
    Connection.release_connection(connection_one)
    connection_two = Connection.create_connection()
    connection_thr = Connection.create_connection()
    connection_fou = Connection.create_connection()
    connection_fiv = Connection.create_connection()
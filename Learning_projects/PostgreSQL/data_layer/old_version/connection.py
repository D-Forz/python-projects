from logger import log
import psycopg2 as bd
import sys

class Connection:
    _DATABASE   = 'db_name'
    _USERNAME   = 'username'
    _PASSWORD   = 'password'
    _DB_PORT    = 'port'
    _HOST       = 'host'
    _connection = None
    _cursor     = None

    @classmethod
    def create_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = bd.connect(
                    user        = cls._USERNAME,
                    password    = cls._PASSWORD,
                    host        = cls._HOST,
                    port        = cls._DB_PORT,
                    database    = cls._DATABASE
                )
                log.debug(f'Connection successfully created: {cls._connection}')
                return cls._connection
            except Exception as e:
                log.error(f'An exception has ocurred in connection: {e}')
                sys.exit()
        else:
            return cls._connection
    
    @classmethod
    def create_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.create_connection().cursor()
                log.debug(f'Cursor successfully created : {cls._cursor}')
            except Exception as e:
                log.error(f'An exception has ocurred in cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

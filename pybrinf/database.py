
'''
Database implementation for PyBrinf.
This module is used to connect to a SQLite database and execute queries.
Docstrings are written in Google style.
'''

import sqlite3
import shutil
import os

from pybrinf.exceptions import DatabaseError


class Database:
    '''Database class core'''
    __conn = None
    __c = None
    connected = property(lambda self: self.__conn is not None)

    def __init__(self, path: str, **kwargs):
        '''Initialize the Database instance.'''
        self.__path = path
        if kwargs.get('bypass', False):
            # If bypass is true, the database will be copied to a temporary directory.
            to_path = kwargs.get('to', None)
            self.__copy(self.__path, to_path)
            self.__path = os.path.join(to_path, self.__path.split('\\')[-1])

    def __copy(self, from_path: str, to_path: str) -> None:
        '''
        Copy a file to another directory.

        Raises:
            DatabaseError: If the file cannot be copied.
        '''
        try:
            shutil.copy(from_path, to_path)
        except Exception as exc:
            raise DatabaseError('Cannot copy the database') from exc

    def __del__(self) -> None:
        '''When the Database instance is deleted, close the connection.'''
        if self.connected:
            self.__conn.close()

    def close(self) -> None:
        '''Close the connection to the database.'''
        if self.connected:
            self.__conn.close()
            self.__conn = None
            self.__c = None
            os.remove(self.__path)

    def connect(self) -> None:
        '''
        Connect to the database.

        Raises:
            DatabaseError: If the database cannot be connected or is already connected.
        '''
        if self.connected:
            raise DatabaseError('Database is already connected')
        try:
            self.__conn = sqlite3.connect(self.__path)
            self.__c = self.__conn.cursor()
        except Exception as exc:
            raise DatabaseError('Cannot connect to the database') from exc

    def execute(self, query: str) -> list:
        '''
        Execute a query.

        Args:
            query (str): The query to execute.
        Raises:
            DatabaseError: If the database is not connected or the query cannot be executed.
        '''
        if not self.connected:
            raise DatabaseError('Database is not connected')
        try:
            self.__c.execute(query)
            return self.__c.fetchall()
        except Exception as exc:
            raise DatabaseError('Cannot execute the query') from exc

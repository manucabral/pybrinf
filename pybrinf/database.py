import sqlite3
import sys, os

from pybrinf.exceptions import *

'''
Database implementation for PyBrinf.
This module is used to connect to a SQLite database and execute queries.
Docstrings are written in Google style.
'''

class Database:
    '''Database class core'''
    __conn = None
    __c = None
    connected = property(lambda self: self.__conn is not None)

    def __init__(self, path: str, **kwargs):
        '''Initialize the Database instance.'''
        self.__path = path
        self.__shutil = kwargs.get('shutil', False)
        if kwargs.get('bypass', False):
            # If bypass is true, the database will be copied to a temporary directory.
            to = kwargs.get('to', None)
            self.__copy(self.__path, to)
            self.__path = to + '\\' + path.split('\\')[-1]
    
    def __copy(self, from_path: str, to_path: str) -> None:
        '''
        Copy a file to another directory.

        Raises:
            FailedToCopyDatabase: If the database cannot be copied.
        '''
        try:
            if self.__shutil:
                # copy large firefox path
                import shutil
                shutil.copy(from_path, to_path)
            else:
                os.system(f'copy "{from_path}" "{to_path}">nul')
        except:
            raise FailedToCopyDatabase()

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
            os.system(f'del "{self.__path}"')

    def connect(self) -> None:
        '''
        Connect to the database.

        Raises:
            DatabaseIsConnected: If the database is already connected.
        '''
        if self.connected:
            raise DatabaseIsConnected()
        try:
            self.__conn = sqlite3.connect(self.__path)
            self.__c = self.__conn.cursor()
        except:
            raise DatabaseIsNotConnected()

    def execute(self, query: str) -> list:
        '''
        Execute a query.

        Args:
            query (str): The query to execute.
        
        Raises:
            DatabaseIsNotConnected: If the database is not connected.
        '''
        if not self.connected:
            raise DatabaseIsNotConnected()
        self.__c.execute(query)
        return self.__c.fetchall()
        
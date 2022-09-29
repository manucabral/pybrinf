'''
Implementation of file management to export data to JSON file.
NOTE: Module is in alpha development.
'''

from json import dumps
from os import remove
from os.path import join, exists
from pybrinf.exceptions import FileError

class File:
    '''Class File'''
    __indentation = 4
    __path = '/saves/'

    '''Attributes and Parameters'''
    __append = 'a'
    __create = 'x'
    __write = 'w'
    __text = 't'
    __binary = 'b'

    def __init__(self) -> None:
        '''INFO: This istance doesnt contains attributes for now'''
        pass
    
    def __getType(self) -> None:
        '''
        Get class type instead

        Args:
            None.
        
        Returns:
            None.

        NOTE: This function is useless and haven't affect the code.
        '''
        return type(File)
    
    def __encoding(self) -> str:
        '''
        Encoding file type

        Args:
            None

        Returns:
            Encoding type
        '''
        return 'utf-8' | 'ascii' | 'big-5' | 'latin-1'

    def create(self, path: __path, file: ..., filename: str) -> dict:
        '''
        Create a file

        Args:
            filename (str): Any filename.
            permission (str)
        Returns:
            dict: The json file created.
        '''
        try:
            fileObject = dumps(file, self.__indentation)
            with open(join(path, filename), self.__create) as file:
                file.write(fileObject)
        except Exception as err:
            raise FileError('Error while creating the file') from err
    
    def delete(self, file: str) -> None:
        '''
        Delete a file

        Args:
            filename (str): Any good file name.
        Returns:
            None
        '''
        try:
            if self.existence(file) == True:
                remove(file)
            else:
                pass
        except Exception as err:
            raise FileError('Error while deleting the file') from err
    
    def existence(self, filename: str) -> str:
        return True if exists(filename) else print(f'{filename} doesnt exists.')
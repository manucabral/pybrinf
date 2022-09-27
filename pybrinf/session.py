'''
    Browser session implementation for PyBrinf.
    This module is used to get session information of a browser.
    Docstrings are written in Google style.
'''

import os

from pybrinf.parser import Parser
from pybrinf.exceptions import SessionError
from pybrinf.commands import CommandType, CommandTabNavigation

class Session:
    '''Session class core.'''

    def __init__(self, path: str):
        '''
        Initialize the Session instance.

        Args:
            path (str): The path of the Session folder.
        Raises:
            SessionError: If the path is not a valid Session folder.
        '''
        self.__path = path + '\\Sessions'
        if not self.__exists:
            raise SessionError('Sessions folder not found')

    @property
    def __exists(self) -> bool:
        '''
        Check if the Sessions path exists

        Returns:
            bool: True if the Sessions path exists, False otherwise.
        '''
        return os.path.exists(self.__path)

    @property
    def __last(self) -> str:
        '''
        Get the last Session file

        Raises:
            SessionError: If the Sessions folder is empty.
        Returns:
            str: The last Session file.
        '''
        files = os.listdir(self.__path)
        sessions = [file.split('_') for file in files if file.startswith('Session')]
        if not sessions:
            raise SessionError('No Session files found')
        sessions = sorted(sessions, key=lambda x: x[1], reverse=True)
        return '_'.join(sessions[0])

    @property
    def filename(self) -> str:
        '''
        Get the session filename

        Returns:
            str: The session filename.
        '''
        return self.__last

    def tabs(self) -> list[CommandTabNavigation]:
        '''
        Get all tabs from the last Session file

        Returns:
            list[CommandTabNavigation]: All updated tabs from the last Session file.
        '''
        file_path = os.path.join(self.__path, self.__last)
        parser = Parser(file_path)
        commands = parser.commands
        commands = parser.filter_command(commands, CommandType.UpdateTabNavigation.value)
        return commands

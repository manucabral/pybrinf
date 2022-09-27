
'''
Browser implementation for PyBrinf.
This module is used to simulate a simple browser.
Docstrings are written in Google style.
'''

import re
import os
import subprocess

from pybrinf.item import Downloaded, History
from pybrinf.database import Database
from pybrinf.utilities import Utilities
from pybrinf.session import Session
from pybrinf.exceptions import BrowserError

class Browser:
    '''
        Browser class core.

        Args:
            **kwargs: The keyword arguments to initialize the browser.
        Attributes:
            name (str): The name of the browser.
            fullname (str): The full name of the browser.
            app_path (str): The path of the browser executable.
            local_path (str): The path of the browser local data.
            process (str): The process name of the browser.
            progid (str): The progid of the browser.
            chromium (bool): Whether the browser is a chromium based browser.
    '''

    def __init__(self, **kwargs):
        '''Initialize the Browser instance.'''
        self.__name = kwargs.get('name', None)
        self.__fullname = kwargs.get('fullname', None)
        self.__app_path = kwargs.get('app_path', None)
        self.__local_path = kwargs.get('local_path', None)
        self.__process = kwargs.get('process', None)
        self.__chromium = kwargs.get('chromium', None)

    def __str__(self):
        '''Get the string representation of the browser.'''
        return f"Browser(name={self.name})"

    def __repr__(self):
        '''Get the string representation of the browser.'''
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        '''Compare the browser with another browser.'''
        return self.name == other.name and self.process == other.process

    @property
    def __history(self) -> Database:
        '''
        Get the history database of the browser.

        Raises:
            BrowserError: If the browser is not installed.
        Returns:
            Database: The history database of the browser.
        '''
        if not self.installed:
            raise BrowserError('The browser is not installed.')
        file = 'History' if self.__chromium else 'places.sqlite'
        path = self.path + '\\' + file
        return Database(
            path=path,
            bypass=True,
            to= os.environ.get('TEMP')
        )

    @property
    def name(self) -> str:
        '''Get the name of the browser.'''
        return self.__name

    @property
    def process(self) -> str:
        '''Get the process of the browser.'''
        return self.__process

    @property
    def fullname(self) -> str:
        '''Get the fullname of the browser.'''
        return self.__fullname

    @property
    def path(self) -> str:
        '''
        Get the full path of the browser.

        Raises:
            BrowserError: If the browser is not installed.
        '''
        base = self.__local_path.split('\\')[0]
        path = self.__local_path.replace(base, os.environ.get(base))
        if self.__chromium:
            return path
        # for now only firefox is supported
        try:
            with open(f'{path}\\profiles.ini', 'r', encoding='utf-8') as file:
                profile = file.readlines()[1].split('=')[1]
                path += "\\Profiles\\" + profile.split('/')[1].strip()
        except Exception as exc:
            raise BrowserError('Error while getting the profile path.') from exc
        return path

    @property
    def app_path(self) -> str:
        '''
        Get the app path of the browser.

        Raises:
            BrowserError: If the browser is not installed.
        '''
        try:
            base = self.__app_path.split('\\')[0]
            return self.__app_path.replace(base, os.environ.get(base))
        except Exception as exc:
            raise BrowserError('Error while getting the app path.') from exc

    @property
    def installed(self) -> bool:
        '''
        Check if the browser is installed.

        Returns:
            bool: True if the browser is installed, False otherwise.
        '''
        return os.path.exists(self.app_path)

    @property
    def running(self) -> bool:
        '''
        Check if the browser is running.

        Returns:
            bool: True if the browser is running, False otherwise.
        '''
        query = Utilities.SEARCH_PROCESS.format(self.process)
        res = subprocess.check_output(query, stderr=subprocess.PIPE).decode()
        return bool(re.search(self.name, res))

    def set_app_path(self, path: str) -> None:
        '''
        Set the app path of the browser.
        IMPORTANT: This method is used when the browser is not in the default app path.

        Args:
            path (str): The path to define.
        '''
        self.__app_path = path

    def set_local_path(self, path: str) -> None:
        '''
        Set the local path of the browser.
        IMPORTANT: This method is used when the browser is not in the default local path.

        Args:
            path (str): The path to define.
        '''
        self.__local_path = path

    def open(self, url: str) -> True:
        '''
        Open the url in the browser.

        Args:
            url (str): The url to open.
        Raises:
            BrowserError: If the browser is not installed or cannot be opened.
        Returns:
            bool: True if the browser is opened, False otherwise.
        '''
        if not self.installed:
            raise BrowserError('The browser is not installed.')
        try:
            subprocess.Popen([self.app_path, url])
            return True
        except Exception as exc:
            raise BrowserError('Error while opening the browser.') from exc
        return False

    def session(self) -> Session:
        '''
            Get the last session of the browser.

            Raises:
                BrowserError: If the browser is not installed or not supported.
        '''
        if not self.installed:
            raise BrowserError('The browser is not installed.')
        if not self.__chromium:
            raise BrowserError('Only chromium based browsers are supported.')
        session = Session(self.path)
        return session

    def close(self) -> True:
        '''
        Close the browser.

        Raises:
            BrowserError: If the browser is not installed or cannot be closed.
        Returns:
            bool: True if the browser is closed, False otherwise.
        '''
        if not self.installed:
            raise BrowserError('The browser is not installed.')
        query = Utilities.KILL_PROCESS.format(self.process)
        try:
            with subprocess.Popen(query, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
                out, err = proc.communicate()
                return bool(not err and out)
        except Exception as exc:
            raise BrowserError('Unknown error while closing the browser.') from exc

    def downloads(self, **kwargs) -> [Downloaded]:
        '''
        Get the list of downloaded items from the browser.

        Args:
            limit (int): The limit of the items to get. Default is 10.
            offset (int): The offset of the items to get. Default is 0.
        Raises:
            BrowserError: If the browser is not installed.
        Returns:
            list(Downloaded): The list of downloaded items.
        '''
        if not self.installed:
            raise BrowserError('The browser is not installed.')
        db_history = self.__history
        db_history.connect()
        res = db_history.execute(Utilities.download_query(self.__chromium, **kwargs))
        downloads = [Downloaded(self.fullname, *download) for download in res]
        db_history.close()
        return downloads

    def history(self, **kwargs) -> [History]:
        '''
        Get the list of history items from the browser.

        Args:
            limit (int): The limit of the items to get.
            offset (int): The offset of the items to get.
        Raises:
            BrowserError: If the browser is not installed.
        Returns:
            list: The history of the browser.
        '''
        if not self.installed:
            raise BrowserError('The browser is not installed.')
        db_history = self.__history
        db_history.connect()
        result = db_history.execute(Utilities.website_query(self.__chromium, **kwargs))
        history = [History(self.fullname, *history) for history in result]
        db_history.close()
        return history

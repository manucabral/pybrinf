import re
import os
import subprocess

from pybrinf.item import Downloaded, History
from pybrinf.database import Database
from pybrinf.constants import Constants
from pybrinf.exceptions import BrowserNotInstalled

'''
Browser implementation for PyBrinf.
This module is used to simulate a simple browser.
Docstrings are written in Google style.
'''

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
        self.__progid = kwargs.get('progid', None)
        self.__process = kwargs.get('process', None)
        self.__chromium = kwargs.get('chromium', None)
        self.__version = kwargs.get('version', None)

    def __str__(self):
        '''Get the string representation of the browser.'''
        return str(self.__class__)
    
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
            BrowserNotInstalled: If the browser is not installed.

        Returns:
            Database: The history database of the browser.
        '''
        if not self.installed:
            raise BrowserNotInstalled()
        path = self.path + '\\History'
        return Database(path, bypass=True, to=os.environ.get('TEMP'))
    
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
        '''Get the full path of the browser.'''
        if self.__chromium:
            base = self.__local_path.split('\\')[0]
            return self.__local_path.replace(base, os.environ.get(base))
    
    @property
    def app_path(self) -> str:
        '''Get the app path of the browser.'''
        try:
            base = self.__app_path.split('\\')[0]
            return self.__app_path.replace(base, os.environ.get(base))
        except:
           return ''
    
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
        query = Constants.SEARCH_PROCESS.format(self.process)
        res = subprocess.check_output(query, stderr=subprocess.PIPE).decode()
        return bool(re.search(self.name, res))
        

    def open(self, url: str) -> True:
        '''
        Open the url in the browser.

        Args:
            url (str): The url to open.
        
        Raises:
            BrowserNotInstalled: If the browser is not installed.
        
        Returns:
            bool: True if the browser is opened, False otherwise.
        '''
        if not self.installed:
            raise BrowserNotInstalled()
        subprocess.Popen([self.app_path, url])
    
    def downloads(self, **kwargs) -> list:
        '''
        Get the list of downloaded items from the browser.

        Args:
            limit (int): The limit of the items to get. Default is 10.
            offset (int): The offset of the items to get. Default is 0.
        
        Raises:
            BrowserNotInstalled: If the browser is not installed.
        
        Returns:
            list(DownloadedItem): The list of downloaded items.
        '''
        if not self.installed:
            raise BrowserNotInstalled()
        db_history = self.__history
        db_history.connect()
        result = db_history.execute(Constants.download_query(**kwargs))
        downloads = [Downloaded(*download) for download in result]
        db_history.close()
        return downloads
    
    def history(self, **kwargs) -> list:
        '''
        Get the history of the browser.

        Args:
            limit (int): The limit of the items to get. Default is 10.
            offset (int): The offset of the items to get. Default is 0.

        Raises:
            BrowserNotInstalled: If the browser is not installed.

        Returns:
            list: The history of the browser.
        '''
        if not self.installed:
            raise BrowserNotInstalled()
        db_history = self.__history
        db_history.connect()
        result = db_history.execute(Constants.history_query(**kwargs))
        history = [History(*history) for history in result]
        return history
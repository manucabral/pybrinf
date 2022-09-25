import re
import os
import subprocess

from pybrinf.item import Downloaded, History
from pybrinf.database import Database
from pybrinf.utilities import Utilities
from pybrinf.exceptions import BrowserNotInstalled, BrowserNotRunning

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
            BrowserNotInstalled: If the browser is not installed.

        Returns:
            Database: The history database of the browser.
        '''
        if not self.installed:
            raise BrowserNotInstalled()
        file = 'History' if self.__chromium else 'places.sqlite'
        path = self.path + '\\' + file
        return Database(
            path= path, 
            bypass= True, 
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
        '''Get the full path of the browser.'''
        base = self.__local_path.split('\\')[0]
        path = self.__local_path.replace(base, os.environ.get(base))
        if self.__chromium:
            return path
        else:
            # for now only firefox is supported
            try:
                with open(f'{path}\\profiles.ini', 'r') as file:
                    profile = file.readlines()[1].split('=')[1]
                    path += "\\Profiles\\" + profile.split('/')[1].strip()
            except:
                raise Exception('Unknown error while getting the profile path.')
        return path
    
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
    
    @property
    def current_website(self):
        '''
        Get the current tab title of the browser.
        NOTE: If you rename the window browser, the title will be the new name.

        Raises:
            BrowserNotInstalled: If the browser is not installed.

        Returns:
            str: The current website of the browser.
        '''
        if not self.installed:
            raise BrowserNotInstalled()
        if not self.running:
            raise BrowserNotRunning()
        query = Utilities.SEARCH_TITLE.format(self.process)
        res = subprocess.check_output(query, stderr=subprocess.PIPE).decode('unicode_escape')
        # TODO: Implement history db parsing
        for line in res.splitlines():
            if 'Window Title:' in line:
                return line.split('Window Title:')[1].strip()
        return ''

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
    
    def close(self) -> True:
        '''
        Close the browser.

        Raises:
            BrowserNotInstalled: If the browser is not installed.
        
        Returns:
            bool: True if the browser is closed, False otherwise.
        '''
        if not self.installed:
            raise BrowserNotInstalled()
        query = Utilities.KILL_PROCESS.format(self.process)
        try:
            p = subprocess.Popen(query, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            return bool(not err and out)
        except:
            raise Exception('Unknown error while closing the browser.')
    
    def downloads(self, **kwargs) -> [Downloaded]:
        '''
        Get the list of downloaded items from the browser.

        Args:
            limit (int): The limit of the items to get. Default is 10.
            offset (int): The offset of the items to get. Default is 0.
        
        Raises:
            BrowserNotInstalled: If the browser is not installed.
        
        Returns:
            list(Downloaded): The list of downloaded items.
        '''
        if not self.installed:
            raise BrowserNotInstalled()

        db_history = self.__history
        db_history.connect()
        ts_epoch = 11644473600 if self.__chromium else 0
        result = db_history.execute(Utilities.download_query(self.__chromium, **kwargs))
        downloads = [Downloaded(*download, ts_epoch=ts_epoch, browser=self.fullname) for download in result]
        db_history.close()
        return downloads
    
    def websites(self, **kwargs) -> [History]:
        '''
        Get the list of visited websites from the browser.

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
        ts_epoch = 11644473600 if self.__chromium else 0
        result = db_history.execute(Utilities.website_query(self.__chromium, **kwargs))
        history = [History(*history, ts_epoch=ts_epoch, browser=self.fullname) for history in result]
        db_history.close()
        return history
        
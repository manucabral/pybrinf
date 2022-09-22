import re
import os
import subprocess
from pybrinf.exceptions import BrowserNotInstalled

class Browser:
    '''Core for the browser module.'''

    def __init__(self, **kwargs):
        '''Initialize the Browser instance.'''
        self.__name = kwargs.get('name', None)
        self.__process = kwargs.get('process', None)
        self.__fullname = kwargs.get('fullname', None)
        self.__app_path = kwargs.get('app_path', None)
        self.__local_path = kwargs.get('local_path', None)
        self.__progid = kwargs.get('progid', None)
        self.__chromium = kwargs.get('chromium', None)

    def __str__(self):
        '''Get the string representation of the browser.'''
        return f'<brinf.__main__.Browser name={self.name} process={self.process}>'
    
    def __repr__(self):
        '''Get the string representation of the browser.'''
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        '''Compare the browser with another browser.'''
        return self.name == other.name and self.process == other.process

    @property
    def installed(self) -> bool:
        '''Check if the browser is installed.'''
        return os.path.exists(self.app_path)

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
        
    def open(self, url: str) -> None:
        '''Open the url in the browser.'''
        if not self.installed:
            raise BrowserNotInstalled()
        subprocess.Popen([self.app_path, url])
        
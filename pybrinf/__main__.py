
import re
import winreg
import platform

from pybrinf.browser import Browser
from pybrinf.register import Register
from pybrinf.database import Database
from pybrinf.utilities import Utilities
from pybrinf.exceptions import *

'''
    Main class of PyBrinf.
    Brinf is a class that allows you to get information about the browser.
    Docstrings are written in Google style.
'''

class Brinf:
    '''Main class for PyBrinf.'''
    __initialize = False
    __os = 'Unknown'

    def __init__(self):
        '''Initialize the Brinf instance.'''
        self.__register = Register()
        self.__utils = Utilities()

    @property
    def __progid(self) -> str:
        '''
        Get the progid value from the registry.

        Raises:
            FileNotFoundError: The registry key could not be found.
        
        Returns:
            str: The progid value of the default browser.
            
        '''
        try:
            key = self.__register.openkey(winreg.HKEY_CURRENT_USER, self.__utils.DEFAULT_BROWSER_KEY)
            return self.__register.extract(key, 'ProgId')
        except FileNotFoundError:
            return None

    def __detect_browser(self, progid: str) -> dict:
        '''
        Detect the browser from the progid.

        Args:
            progid (str): The progid of the browser.
        
        Raises:
            BrowserNotDetected: The browser could not be detected.

        Returns:
            dict: The browser information.
        '''
        for browser in self.__utils.BROWSERS:
            if re.search(browser.get('name'), progid, re.IGNORECASE):
                return browser
        raise BrowserNotDetected()
        

    def init(self) -> None:
        '''
        This method must be called before using any other methods of the class.

        Raises:
            SystemNotSupported: The system is not supported.
            BrowserNotFound: The default browser could not be found.
        '''
        self.__os = platform.system()
        if not self.__os in self.__utils.SUPPORTED_SYSTEMS:
            raise SystemNotSupported(self.__os)
        key = self.__progid
        if key:
            self.__browser = Browser(**self.__detect_browser(key))
            self.__initialize = True
        else:
            raise BrowserNotFound()

    @property
    def default_browser(self) -> Browser:
        '''
        Get the default browser instance.

        Raises:
            BrinfNotInitialized: The Brinf instance is not initialized.
        
        Returns:
            browser: The default browser of the system.
        '''
        if not self.__initialize:
            raise BrinfNotInitialized()
        return self.__browser
    
    def browser(self, name: str) -> Browser:
        '''
        Get a browser instance from the name.
        If the browser is not installed, it will raise an exception.

        Args:
            name (str): The name of the browser.
        
        Raises:
            BrowserNotFound: The browser could not be found.

        Returns:
            browser: The browser.
        '''
        if not self.__initialize:
            raise BrinfNotInitialized()
        try:
            data = self.__utils.get_browser_data(name)
            return Browser(**data)
        except BrowserNotFound:
            raise BrowserNotFound()
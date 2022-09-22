
from pybrinf.browser import Browser
from pybrinf.register import Register
from pybrinf.constants import Constants
from pybrinf.exceptions import *

from re import search, IGNORECASE
from winreg import HKEY_CURRENT_USER, KEY_READ

class Brinf:
    '''Core for the Brinf module.'''
    __initialize = False

    def __init__(self):
        '''Initialize the Brinf instance.'''
        self.__register = Register()
        self.__constants = Constants()
    
    def init(self):
        '''
        This method must be called before using any other methods 
        because it detects the default browser.
        '''
        key = self.__progid
        if key:
            self.browser = Browser(**self.__detect_browser(key))
            self.__initialize = True
        else:
            raise BrowserNotDetected()

    @property
    def default_browser(self) -> Browser:
        '''
        Get the default browser of the system.

        returns:
            The default browser.
        '''
        if not self.__initialize:
            raise BrinfNotInitialized()
        return self.browser

    @property
    def __progid(self):
        '''
        Get the progid of the default browser.

        returns:
            The progid of the default browser.
        '''
        key = self.__register.openkey(HKEY_CURRENT_USER, self.__constants.DEFAULT_BROWSER_KEY)
        return self.__register.extract(key, 'ProgId')

    def __detect_browser(self, progid: str) -> dict:
        '''
        Detect the browser from the progid.

        params:
            progid: The progid to detect the browser from.
        
        returns:
            The detected browser.
        '''
        for browser in self.__constants.BROWSERS:
            if search(browser.get('name'), progid, IGNORECASE):
                return browser
        raise BrowserNotDetected()

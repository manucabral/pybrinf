
import re
import winreg
import platform
from typing import Union

from pybrinf.browser import Browser
from pybrinf.register import Register
from pybrinf.database import Database
from pybrinf.utilities import Utilities
from pybrinf.item import History, Downloaded
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

    def __detect_browser(self, progid: str) -> {}:
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

    def reset(self) -> None:
        '''Reset the Brinf instance.'''
        self.__initialize = False
        self.__os = 'Unknown'
        self.__browser = None

    def installed_browsers(self, exclude: Union[str, list] = []) -> [Browser]:
        '''
        Get a list of installed browsers.

        Args:
            exclude (str, list of str): Exclude especific browsers from the list.

        Raises:
            BrinfNotInitialized: The Brinf instance has not been initialized.
            BrowserNotFound: None browser could be found.

        Returns:
            list: The list of installed browsers.
        '''
        if not self.__initialize:
            raise BrinfNotInitialized()
        if isinstance(exclude, str):
            exclude = list(exclude)
        
        browsers = []
        for browser in self.__utils.BROWSERS:
            instance = Browser(**browser)
            if instance.installed and not instance.name in exclude:
                browsers.append(instance)
        if len(browsers) == 0:
            raise BrowserNotFound()
        
        return browsers

    @property
    def supported_browsers(self) -> [str]:
        '''
        Get the list of supported browsers.

        Returns:
            list: The list of supported browsers.
        '''
        return self.__utils.SUPPORTED_BROWSERS

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


    def history(self, reverse: bool=True, **kwargs) -> [History]:
        '''
        Get the history of all browsers.
        IMPORTANT: Please limit the number of results to avoid performance issues.

        Args:
            reverse (bool): If True, the history will be sorted in reverse order. Defaults to True.
            exclude (str, list of str): Exclude especific browsers from the history.
            limit (int): The maximum number of history items for each browser.
            offset (int): The offset of the history items for each browser.

        Raises:
            BrinfNotInitialized: The Brinf instance is not initialized.

        Returns:
            list: The history of the default browser.
        '''
        if not self.__initialize:
            raise BrinfNotInitialized()
        browsers = self.installed_browsers(kwargs.get('exclude', []))
        history = []
        for browser in browsers:
            browser_websites = browser.websites(**kwargs)
            if len(browser_websites) == 0:
                continue
            history += browser_websites
        return sorted(history, key=lambda x: Utilities.date_to_int(x.last_visit), reverse=reverse)

    def downloads(self, reverse: bool=True, **kwargs) -> [Downloaded]:
        '''
        Get the downloads of all browsers.
        IMPORTANT: Please limit the number of results to avoid performance issues.

        Args:
            reverse (bool): If True, the downloads will be sorted in reverse order. Defaults to True.
            exclude (str, list of str): Exclude especific browsers from the downloads.
            limit (int): The maximum number of downloads items for each browser.
            offset (int): The offset of the downloads items for each browser.

        Raises:
            BrinfNotInitialized: The Brinf instance is not initialized.

        Returns:
            list: The downloads of the default browser.
        '''
        if not self.__initialize:
            raise BrinfNotInitialized()
        browsers = self.installed_browsers(kwargs.get('exclude', []))
        downloads = []
        for browser in browsers:
            browser_downloads = browser.downloads(**kwargs)
            if len(browser_downloads) == 0:
                continue
            downloads += browser_downloads
        return sorted(downloads, key=lambda x: Utilities.date_to_int(x.start_time), reverse=reverse)

    def browser(self, name: str) -> Browser:
        '''
        Get a browser instance from the name.
        If the browser is not installed, it will raise an exception.

        Args:
            name (str): The name of the browser.
        
        Raises:
            BrowserNotFound: The browser could not be found.
            BrowserNotSupported: The browser is not supported.

        Returns:
            browser: The browser.
        '''
        if not self.__initialize:
            raise BrinfNotInitialized()
        if not name in self.__utils.SUPPORTED_BROWSERS:
            raise BrowserNotSupported(name)
        try:
            data = self.__utils.get_browser_data(name)
            return Browser(**data)
        except:
            raise BrowserNotFound()
        
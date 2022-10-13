'''
    Main class of PyBrinf.
    Brinf is a class that allows you to get information about the browser.
    Docstrings are written in Google style.
'''

import re
from typing import Union

from pybrinf.browser import Browser
from pybrinf.utilities import Utilities
from pybrinf.item import History, Downloaded
from pybrinf.exceptions import BrowserError, BrinfError, SystemBrinfError

# import some utils for Windows systems
if Utilities.system() == 'win32':
    import winreg
    from pybrinf.register import Register
elif Utilities.system() == 'linux':
    import subprocess


class Brinf:
    '''Main class for PyBrinf.'''
    __initialize = False
    __browser = None
    __os = Utilities.system()

    def __init__(self):
        '''Initialize the Brinf instance.'''
        self.__utils = Utilities()

    @property
    def __default_win_browser(self) -> dict:
        '''
        Get the default browser of Windows system.

        Raises:
            FileNotFoundError: The registry key could not be found.
            BrowserError: The default browser could not be found.
        '''
        if self.__os == 'win32':
            register = Register()
            hkey = winreg.HKEY_CURRENT_USER
            key = register.openkey(hkey, self.__utils.DEFAULT_BROWSER_KEY)
            progid = register.extract(key, 'ProgId')
            for browser in self.__utils.BROWSERS:
                if re.search(browser['name'], progid, re.IGNORECASE):
                    return browser
            raise BrowserError('The default browser could not be found.')
        return {}

    @property
    def __default_linux_browser(self) -> dict:
        '''
        Get the default browser of Linux system.

        Raises:
            SystemBrinfError: A system error occurred while getting the default browser.
            BrowserError: The default browser could not be found or is not supported.
        Returns:
            dict: The default browser.
        '''
        if self.__os == 'linux':
            process = subprocess.Popen(
                self.__utils.LINUX_DEFAULT_BROWSER, stdout=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                raise SystemBrinfError(error)
            browser = output.decode().strip()
            browser_data = None
            for data in self.__utils.BROWSERS:
                if re.search(data['name'], browser, re.IGNORECASE):
                    browser_data = data
                    break
            if browser_data is None:
                raise BrowserError('The default browser could not be found.')
            if not self.__os in browser_data['os_support']:
                raise BrowserError(
                    f'{data["fullname"]} is not supported in {self.__os}. Sorry!')
            return data
        return {}

    def init(self) -> None:
        '''
        This method must be called before using any other methods of the class.

        Raises:
            SystemBrinfError: The system is not supported.
            BrowserError: The default browser could not be found.
        '''
        if self.__os not in self.__utils.SUPPORTED_SYSTEMS:
            raise SystemBrinfError(f'System {self.__os} is not supported.')
        detector = {
            'win32': self.__default_win_browser,
            'linux': self.__default_linux_browser
        }
        self.__browser = Browser(self.__os, **detector[self.__os])
        self.__initialize = True

    def reset(self) -> None:
        '''Reset the Brinf instance.'''
        self.__initialize = False
        self.__os = 'Unknown'
        self.__browser = None

    def installed_browsers(self, exclude: Union[str, list] = '') -> list[Browser]:
        '''
        Get a list of installed browsers.

        Args:
            exclude (str, list of str): Exclude especific browsers from the list.
        Raises:
            BrinfError: The Brinf instance has not been initialized.
            BrowserError: None browser could be found.
        Returns:
            list: The list of installed browsers.
        '''
        if not self.__initialize:
            raise BrinfError('The Brinf instance is not initialized.')
        if isinstance(exclude, str):
            exclude = list(exclude)
        browsers = []
        for browser in self.__utils.BROWSERS:
            instance = Browser(**browser)
            if instance.installed and not instance.name in exclude:
                browsers.append(instance)
        if len(browsers) == 0:
            raise BrowserError('None browser could be found.')
        return browsers

    @property
    def supported_browsers(self) -> list[str]:
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
            raise BrinfError('The Brinf instance is not initialized.')
        return self.__browser

    def history(self, reverse: bool = True, **kwargs) -> list[History]:
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
            raise BrinfError('The Brinf instance is not initialized.')
        browsers = self.installed_browsers(kwargs.get('exclude', []))
        history = []
        for browser in browsers:
            browser_websites = browser.history(**kwargs)
            if len(browser_websites) == 0:
                continue
            history += browser_websites
        return sorted(history, key=lambda x: Utilities.date_to_int(x.last_visit), reverse=reverse)

    def downloads(self, reverse: bool = True, **kwargs) -> list[Downloaded]:
        '''
        Get the downloads of all browsers.
        IMPORTANT: Please limit the number of results to avoid performance issues.

        Args:
            reverse (bool): If True, the downloads will be sorted in reverse order.
            exclude (str, list of str): Exclude especific browsers from the downloads.
            limit (int): The maximum number of downloads items for each browser.
            offset (int): The offset of the downloads items for each browser.
        Raises:
            BrinfNotInitialized: The Brinf instance is not initialized.
        Returns:
            list: The downloads of the default browser.
        '''
        if not self.__initialize:
            raise BrinfError('The Brinf instance is not initialized.')
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
            BrinfError: The Brinf instance is not initialized.
            BrowserError: The browser could not be found or the browser is not supported.
        Returns:
            browser: The browser.
        '''
        if not self.__initialize:
            raise BrinfError('The Brinf instance is not initialized.')
        if not name in self.__utils.SUPPORTED_BROWSERS:
            raise BrowserError(f'The browser {name} is not supported.')
        try:
            data = self.__utils.get_browser_data(name)
            return Browser(self.__os, **data)
        except Exception as exc:
            raise BrowserError('The browser could not be found.') from exc

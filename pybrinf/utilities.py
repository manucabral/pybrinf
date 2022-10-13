'''
This module contains all utility functions used in PyBrinf.
TODO: Add linux and macos complete support.
'''

import sys
from datetime import datetime, timedelta
from pybrinf.exceptions import BrowserError
from pybrinf.browsers import BROWSERS
from pybrinf.queries import (
    DOWNLOAD_QUERY,
    MOZ_DOWNLOAD_QUERY,
    MOZ_WEBSITE_QUERY,
    WEBSITE_QUERY,
)


class Utilities:
    '''Utilities class for PyBrinf.'''

    BROWSERS = BROWSERS
    SUPPORTED_SYSTEMS = ['win32', 'linux']
    SUPPORTED_BROWSERS = ['chrome', 'edge', 'yandex',
                          'firefox', 'opera', 'brave', 'vivaldi']
    DEFAULT_BROWSER_KEY = \
        'Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice'

    LINUX_DEFAULT_BROWSER = 'xdg-settings get default-web-browser'.split()
    KILL_PROCESS = 'taskkill /f /im {}'
    SEARCH_PROCESS = 'WMIC PROCESS WHERE "name=\'{}\'" GET ExecutablePath'
    SEARCH_TITLE = 'tasklist /fi "imagename eq {}" /fo list /v'

    @staticmethod
    def system() -> str:
        '''
        Get the system name.

        Returns:
            str: The system name, e.g. win32, linux, etc
        '''
        return sys.platform

    @staticmethod
    def set_filter(query: str, **kwargs) -> str:
        '''
        Set the filter for the query.

        Args:
            query (str): The query to filter.
            **kwargs: The filter to apply.

        Returns:
            str: The filtered query.
        '''
        query += f'LIMIT {kwargs["limit"] if kwargs.get("limit") else -1}'
        query += f' OFFSET {kwargs["offset"] if kwargs.get("offset") else 0}'
        return query

    @staticmethod
    def website_query(chromium: bool, **kwargs) -> str:
        '''
        Get the history query with the given parameters.

        Args:
            chromium (bool): If the browser is chromium based.
            limit (int): The limit of the items to get.
            offset (int): The offset of the items to get.

        Returns:
            str: The history query.
        '''
        query = WEBSITE_QUERY if chromium else MOZ_WEBSITE_QUERY
        return Utilities.set_filter(query, **kwargs)

    @staticmethod
    def download_query(chromium: bool, **kwargs) -> str:
        '''
        Get the query for downloads.

        Args:
            chromium (bool): If the browser is chromium based.
            limit (int): The limit of the items to get.
            offset (int): The offset of the items to get.
        Returns:
            str: The query for downloads.
        '''
        query = DOWNLOAD_QUERY if chromium else MOZ_DOWNLOAD_QUERY
        return Utilities.set_filter(query, **kwargs)

    @staticmethod
    def get_browser_data(name: str) -> dict:
        '''
        Get the data of a browser.

        Args:
            name (str): The name of the browser.
        Returns:
            dict: The data of the browser.
        '''
        for browser in BROWSERS:
            if browser['name'].lower() == name.lower():
                return browser
        raise BrowserError('The browser is not supported.')

    @staticmethod
    def date_to_int(date: datetime) -> int:
        '''
        Convert a datetime object to an integer.

        Args:
            date (datetime): The datetime object to convert.

        Returns:
            int: The integer representation of the datetime object.
        '''
        return int(date.strftime("%Y%m%d%H%M%S"))

    @staticmethod
    def webkit_to_date(webkit: int) -> datetime:
        '''
        Convert a webkit timestamp to a datetime object.
        Source: https://www.epochconverter.com/webkit

        Args:
            webkit (int): The webkit timestamp to convert.
        Returns:
            datetime: The datetime object.
        '''
        epoch_start = datetime(1601, 1, 1)
        delta = timedelta(microseconds=webkit)
        return epoch_start + delta

    @staticmethod
    def unix_to_date(unix: int) -> datetime:
        '''
        Convert a unix timestamp to a datetime object.

        Args:
            unix (int): The unix timestamp to convert.
        Returns:
            datetime: The datetime object.
        '''
        if not unix:
            return datetime.now()
        unix_time = unix / 1000000
        epoch = datetime.utcfromtimestamp(0)
        return epoch + timedelta(seconds=unix_time)

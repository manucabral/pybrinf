from pybrinf.exceptions import BrowserNotFound
from pybrinf.browsers import BROWSERS
from pybrinf.queries import (
    DOWNLOAD_QUERY,
    MOZ_DOWNLOAD_QUERY,
    MOZ_WEBSITE_QUERY,
    WEBSITE_QUERY,
)

'''
Contants values for PyBrinf.
TODO: Add more browsers and linux / macos support.
TODO: Modify the constants to be more dynamic for future browsers support.
'''

class Constants:
    '''Constants class for PyBrinf.'''

    BROWSERS = BROWSERS
    DEFAULT_BROWSER_KEY = 'Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice'
    SUPPORTED_SYSTEMS = ['Windows']
    SUPPORTED_BROWSERS = ['chrome', 'edge', 'yandex', 'firefox']
    KILL_PROCESS = 'taskkill /f /im {}'
    SEARCH_PROCESS = 'WMIC PROCESS WHERE "name=\'{}\'" GET ExecutablePath'
    SEARCH_TITLE = 'tasklist /fi "imagename eq {}" /fo list /v'

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
        query += f' LIMIT {kwargs["limit"] if kwargs.get("limit") else 10}'
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
        return Constants.set_filter(query, **kwargs)

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
        return Constants.set_filter(query, **kwargs)

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
        raise BrowserNotFound()
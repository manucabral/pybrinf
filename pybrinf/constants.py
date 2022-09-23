from pybrinf.exceptions import BrowserNotFound

'''
Contants values for PyBrinf.
TODO: Add more browsers and linux / macos support.
TODO: Modify the constants to be more dynamic for future browsers support.
'''
class Constants:
    '''Constants class for PyBrinf.'''

    DEFAULT_BROWSER_KEY = 'Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice'
    SUPPORTED_SYSTEMS = ['Windows']
    SUPPORTED_BROWSERS = ['chrome', 'edge', 'yandex']
    KILL_PROCESS = 'taskkill /f /im {}'
    SEARCH_PROCESS = 'WMIC PROCESS WHERE "name=\'{}\'" GET ExecutablePath'
    SEARCH_TITLE = 'tasklist /fi "imagename eq {}" /fo list /v'
    #tasklist /fi "imagename eq browser.exe" /fo list /v | find /i "Window Title:"
    BROWSERS = [
        {
            'name': 'Chrome',
            'fullname': 'Google Chrome',
            'process': 'chrome.exe',
            'progid': 'ChromeHTML',
            'chromium': True,
            'local_path': '\\Google\\Chrome\\User Data\\Default'
        },
        {
            'name': 'Firefox',
            'fullname': 'Mozilla Firefox',
            'process': 'firefox.exe',
            'progid': 'FirefoxHTML',
            'chromium': False,
            'local_path': '\\Mozilla\\Firefox\\Profiles\\'
        },
        {
            'name': 'Edge',
            'fullname': 'Microsoft Edge',
            'process': 'msedge.exe',
            'progid': 'EdgeHTML',
            'chromium': True,
            'app_path': 'ProgramFiles(x86)\\Microsoft\\Edge\\Application\\msedge.exe',
            'local_path': 'LOCALAPPDATA\\Microsoft\\Edge\\User Data\\Default'
        },
        {
            'name': 'Yandex',
            'fullname': 'Yandex Browser',
            'process': 'browser.exe',
            'chromium': True,
            'progid': 'YandexHTML',
            'app_path': 'LOCALAPPDATA\\Yandex\\YandexBrowser\\Application\\browser.exe',
            'local_path': 'LOCALAPPDATA\\Yandex\\YandexBrowser\\User Data\\Default'
        }
    ]

    WEBSITE_QUERY = '''
SELECT url, title, visit_count, last_visit_time
FROM urls
ORDER BY last_visit_time DESC
'''

    DOWNLOAD_QUERY = '''
SELECT total_bytes, current_path, start_time, end_time, tab_url, url
FROM downloads
LEFT JOIN downloads_url_chains
ON downloads.id = downloads_url_chains.id
ORDER BY start_time DESC
'''

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
    def website_query(**kwargs) -> str:
        '''
        Get the history query with the given parameters.

        Args:
            limit (int): The limit of the items to get. 
            offset (int): The offset of the items to get.

        Returns:
            str: The history query.
        '''
        return Constants.set_filter(Constants.WEBSITE_QUERY, **kwargs)

    @staticmethod
    def download_query(**kwargs) -> str:
        '''
        Get the query for downloads.

        Args:
            limit (int): The limit of the items to get.
            offset (int): The offset of the items to get.
        
        Returns:
            str: The query for downloads.
        '''
        return Constants.set_filter(Constants.DOWNLOAD_QUERY, **kwargs)

    @staticmethod
    def get_browser_data(name: str) -> dict:
        '''
        Get the data of a browser.

        Args:
            name (str): The name of the browser.
        
        Returns:
            dict: The data of the browser.
        '''
        for browser in Constants.BROWSERS:
            if browser.get('name').lower() == name.lower():
                return browser
        raise BrowserNotFound()
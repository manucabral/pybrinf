from pybrinf.exceptions import BrowserNotFound

'''
Contants values for PyBrinf.
TODO: Add more browsers and linux / macos support.
'''
class Constants:
    '''Constants class for PyBrinf.'''

    DEFAULT_BROWSER_KEY = 'Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice'
    SUPPORTED_SYSTEMS = ['Windows']
    SEARCH_PROCESS = 'WMIC PROCESS WHERE "name=\'{}\'" GET ExecutablePath'

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

    DOWNLOADS_QUERY = '''
SELECT total_bytes, current_path, start_time, end_time, tab_url, url
FROM downloads
LEFT JOIN downloads_url_chains
ON downloads.id = downloads_url_chains.id
'''

    @staticmethod
    def download_query(**kwargs) -> str:
        '''
        Get the query for downloads.
        TODO: Implement limit, offset, and filters.

        Returns:
            str: The query for downloads.
        '''
        return Constants.DOWNLOADS_QUERY

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
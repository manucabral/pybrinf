from pybrinf.exceptions import BrowserNotDetected

class Constants:
    DEFAULT_BROWSER_KEY = 'Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice'

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

    @staticmethod
    def get_browser_data(name: str) -> dict:
        '''
        Get the data of a browser.

        params:
            name: The name of the browser to get.

        returns:
            The browser.
        '''
        for browser in Constants.BROWSERS:
            if browser.get('name') == name:
                return browser
        raise BrowserNotDetected()
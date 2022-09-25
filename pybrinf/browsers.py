'''
This file contains all browser necessary data.
NOTE: For now only supports Windows Systems.
'''

BROWSERS = [
    {
        'name': 'Chrome',
        'fullname': 'Google Chrome',
        'process': 'chrome.exe',
        'progid': 'ChromeHTML',
        'chromium': True,
        'app_path': 'ProgramFiles\\Google\\Chrome\\Application\\chrome.exe',
        'local_path': 'LOCALAPPDATA\\Google\\Chrome\\User Data\\Default'
    },
    {
        'name': 'Firefox',
        'fullname': 'Mozilla Firefox',
        'process': 'firefox.exe',
        'progid': 'FirefoxHTML',
        'chromium': False,
        'app_path': 'ProgramFiles\\Mozilla Firefox\\firefox.exe',
        'local_path': 'APPDATA\\Mozilla\\Firefox'
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
    },
    {
        'name': 'Opera',
        'fullname': 'Opera',
        'process': 'opera.exe',
        'chromium': True,
        'progid': 'OperaHTML',
        'app_path': 'LOCALAPPDATA\\Programs\\Opera\\launcher.exe',
        'local_path': 'APPDATA\\Opera Software\\Opera Stable'
    }
]
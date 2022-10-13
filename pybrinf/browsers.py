'''
This file contains all browser necessary data.
NOTE:
    Windows supports all browsers.
    Linux only supports Chrome and Firefox.
    MacOS not supported yet.
'''

BROWSERS = [
    {
        'name': 'Chrome',
        'fullname': 'Google Chrome',
        'process': {
            'win32': 'chrome.exe',
            'linux': 'google-chrome'
        },
        'progid': 'ChromeHTML',
        'chromium': True,
        'app_path': {
            'win32': 'ProgramFiles/Google/Chrome/Application/chrome.exe',
            'linux': 'HOME/usr/bin/google-chrome-stable'
        },
        'local_path': {
            'win32': 'LOCALAPPDATA/Google/Chrome/User Data/Default',
            'linux': 'HOME/.config/google-chrome/Default'
        },
        'os_support': ['win32', 'linux']
    },
    {
        'name': 'Firefox',
        'fullname': 'Mozilla Firefox',
        'process': {
            'win32': 'firefox.exe',
            'linux': 'firefox'
        },
        'progid': 'FirefoxHTML',
        'chromium': False,
        'app_path': {
            'win32': 'ProgramFiles/Mozilla Firefox/firefox.exe',
            'linux': 'HOME/usr/bin/firefox'
        },
        'local_path': {
            'win32': 'APPDATA/Mozilla/Firefox',
            'linux': 'HOME/.mozilla/firefox'
        },
        'os_support': ['win32', 'linux']
    },
    {
        'name': 'Edge',
        'fullname': 'Microsoft Edge',
        'process': 'msedge.exe',
        'progid': 'EdgeHTML',
        'chromium': True,
        'app_path': 'ProgramFiles(x86)/Microsoft/Edge/Application/msedge.exe',
        'local_path': 'LOCALAPPDATA/Microsoft/Edge/User Data/Default',
        'os_support': ['win32']
    },
    {
        'name': 'Yandex',
        'fullname': 'Yandex Browser',
        'process': 'browser.exe',
        'chromium': True,
        'progid': 'YandexHTML',
        'app_path': 'LOCALAPPDATA/Yandex/YandexBrowser/Application/browser.exe',
        'local_path': 'LOCALAPPDATA/Yandex/YandexBrowser/User Data/Default',
        'os_support': ['win32']
    },
    {
        'name': 'Opera',
        'fullname': 'Opera',
        'process': 'opera.exe',
        'chromium': True,
        'progid': 'OperaHTML',
        'app_path': 'LOCALAPPDATA/Programs/Opera/launcher.exe',
        'local_path': 'APPDATA/Opera Software/Opera Stable',
        'os_support': ['win32']
    },
    {
        'name': 'Brave',
        'fullname': 'Brave Browser',
        'process': 'brave.exe',
        'chromium': True,
        'progid': 'BraveHTML',
        'app_path': 'ProgramFiles/BraveSoftware/Brave-Browser/Application/brave.exe',
        'local_path': 'LOCALAPPDATA/BraveSoftware/Brave-Browser/User Data/Default',
        'os_support': ['win32']
    },
    {
        'name': 'Vivaldi',
        'fullname': 'Vivaldi',
        'process': 'vivaldi.exe',
        'chromium': True,
        'progid': 'VivaldiHTML',
        'app_path': 'LOCALAPPDATA/Vivaldi/Application/vivaldi.exe',
        'local_path': 'LOCALAPPDATA/Vivaldi/User Data/Default',
        'os_support': ['win32']
    }
]

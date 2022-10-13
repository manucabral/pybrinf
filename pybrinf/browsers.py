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
        'process': {
            'win32': 'msedge.exe',
            'linux': 'msedge'
        },
        'progid': 'EdgeHTML',
        'chromium': True,
        'app_path': {
            'win32': 'ProgramFiles(x86)/Microsoft/Edge/Application/msedge.exe',
            'linux': 'sure?'
        },
        'local_path': {
            'win32': 'LOCALAPPDATA/Microsoft/Edge/User Data/Default',
            'linux': 'sure?'
        },
        'os_support': ['win32']
    },
    {
        'name': 'Yandex',
        'fullname': 'Yandex Browser',
        'process': {
            'win32': 'browser.exe',
            'linux': 'yandex-browser'
        },
        'chromium': True,
        'progid': 'YandexHTML',
        'app_path': {
            'win32': 'LOCALAPPDATA/Yandex/YandexBrowser/Application/browser.exe',
            'linux': 'HOME/usr/bin/yandex-browser'
        },
        'local_path': {
            'win32': 'LOCALAPPDATA/Yandex/YandexBrowser/User Data/Default',
            'linux': 'HOME/.config/yandex-browser-beta'
        },
        'os_support': ['win32']
    },
    {
        'name': 'Opera',
        'fullname': 'Opera',
        'process': {
            'win32': 'opera.exe',
            'linux': 'opera'
        },
        'chromium': True,
        'progid': 'OperaHTML',
        'app_path': {
            'win32': 'LOCALAPPDATA/Programs/Opera/launcher.exe',
            'linux': 'HOME/usr/bin/opera'
        },
        'local_path': {
            'win32': 'APPDATA/Opera Software/Opera Stable',
            'linux': 'HOME/.config/opera'
        },
        'os_support': ['win32']
    },
    {
        'name': 'Brave',
        'fullname': 'Brave Browser',
        'process': {
            'win32': 'brave.exe',
            'linux': 'brave-browser'
        },
        'chromium': True,
        'progid': 'BraveHTML',
        'app_path': {
            'win32': 'ProgramFiles/BraveSoftware/Brave-Browser/Application/brave.exe',
            'linux': 'HOME/usr/bin/brave-browser'
        },
        'local_path': {
            'win32': 'LOCALAPPDATA/BraveSoftware/Brave-Browser/User Data/Default',
            'linux': 'HOME/.config/BraveSoftware/Brave-Browser'
        },
        'os_support': ['win32']
    },
    {
        'name': 'Vivaldi',
        'fullname': 'Vivaldi',
        'process': {
            'win32': 'vivaldi.exe',
            'linux': 'vivaldi'
        },
        'chromium': True,
        'progid': 'VivaldiHTML',
        'app_path': {
            'win32': 'LOCALAPPDATA/Vivaldi/Application/vivaldi.exe',
            'linux': 'HOME/usr/bin/vivaldi'
        },
        'local_path': {
            'win32': 'LOCALAPPDATA/Vivaldi/User Data/Default',
            'linux': 'HOME/.config/vivaldi'
        },
        'os_support': ['win32']
    }
]

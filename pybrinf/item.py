'''
This module contains the Item class.
The Item class is used to store different types of items (Downloads, History, etc).
Docstrings are written in Google style.
'''

from pybrinf.exceptions import SystemBrinfError
from pybrinf.utilities import Utilities

if Utilities.system() == 'Windows':
    import os

class Item:
    '''Simulates a simple item.'''

    def __init__(self, browser: str):
        '''Initialize the Item instance.'''
        self.browser = browser

    def __str__(self):
        '''Get the string representation of the object.'''
        return str(self.__class__)

    def __repr__(self):
        '''Get the string representation of the object.'''
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        '''Compare the item with another item.'''

class Downloaded(Item):
    '''Simulates a downloaded item.'''

    def __init__(self, *args):
        '''Initialize the Downloaded instance.'''
        super().__init__(args[0])
        self.bytes = args[1]
        self.path = args[2]
        if 'Firefox' in args[0]:
            self.start_time = Utilities.unix_to_date(args[3])
            self.end_time = Utilities.unix_to_date(args[4])
        else:
            self.start_time = Utilities.webkit_to_date(args[3])
            self.end_time = Utilities.webkit_to_date(args[4])
        self.end_time = Utilities.webkit_to_date(args[4])
        self.tab_url = args[5]
        self.url = args[6]
        # self.state = args[7] TODO: Add state

    def __eq__(self, other: object) -> bool:
        '''Compare the downloaded item with another downloaded item.'''
        return self.url == other.url and self.path == other.path

    # NOTE: Exclude until Linux support is added
    def open(self) -> None:
        '''Open the downloaded file.'''
        if Utilities.system() == 'Windows':
            try:
                os.startfile(self.path.replace(self.path.split('\\')[-1], ''))
            except Exception as exc:
                raise SystemBrinfError(exc) from exc
        else:
            raise SystemBrinfError('Unsupported platform')

class History(Item):
    '''Simulates a history item.'''

    def __init__(self, *args):
        '''Initialize the History instance.'''
        super().__init__(args[0])
        self.url = args[1]
        self.title = args[2]
        self.visit_count = args[3]
        if 'Firefox' in self.browser:
            self.last_visit = Utilities.unix_to_date(args[4])
        else:
            self.last_visit = Utilities.webkit_to_date(args[4])

    def __eq__(self, other: object) -> bool:
        '''Compare the history item with another history item.'''
        return self.url == other.url and self.title == other.title

    def is_from(self, domain: str) -> bool:
        '''Check if the tab is from a specific domain.'''
        return domain in self.url

class SessionTab(Item):
    '''Simulates a tab from a session.'''

    def __init__(self, *args):
        '''Initialize the Tab instance.'''
        super().__init__(args[0])
        self.id = args[1]
        self.index = args[2]
        self.url = args[3]
        self.title = args[4]
        self.pinned = False
        self.closed = False
        self.active = False

    def __eq__(self, other: object) -> bool:
        '''Compare the tab with another tab.'''
        return self.id == other.id and self.url == other.url

    @property
    def is_active(self) -> bool:
        '''Check if the tab is active.'''
        return self.active

class Tab(Item):
    '''Simulates a tab from devtools.'''

    # pylint: disable=too-few-public-methods
    def __init__(self, browser: str, **kwargs):
        super().__init__(browser)
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        return f'<Tab {self.id} {self.browser}>'

import os, datetime

'''
This module contains the Item class.
The Item class is used to store different types of items (Downloads, History, etc).
Docstrings are written in Google style.
'''

class Item:
    def __init__(self, ts_epoch: int, browser: str):
        '''Initialize the Item instance.'''
        self.__ts_epoch = ts_epoch
        self.browser = browser
    
    def __str__(self):
        '''Get the string representation of the object.'''
        return str(self.__class__)
    
    def __repr__(self):
        '''Get the string representation of the object.'''
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        '''Compare the item with another item.'''
        pass

    def open(self) -> None:
        '''Open the item.'''
        pass

    def to_datetime(self, time: int) -> datetime.datetime:
        '''
        Get the datetime representation of the downloaded item.

        Args:
            time (int): The integer unix timestamp to convert.
        
        Returns:
            datetime.datetime: The datetime representation of the downloaded item.
        '''
        if not time:
            return datetime.datetime.now()
        tse = (time/1000000) - self.__ts_epoch
        return datetime.datetime.fromtimestamp(tse)

class Downloaded(Item):
    '''Simulates a downloaded item.'''
    def __init__(self,
        bytes: int,
        path: str,
        start: int,
        end: int,
        tab_url: str, 
        url: str,
        ts_epoch: int,
        browser: str
    ):
        '''Initialize the Downloaded instance.'''
        super().__init__(ts_epoch, browser)
        self.bytes = bytes
        self.start_time = self.to_datetime(start)
        self.end_time = self.to_datetime(end)
        self.path = path
        self.url = url
        self.tab_url = tab_url

    def __eq__(self, other: object) -> bool:
        '''Compare the downloaded item with another downloaded item.'''
        return self.url == other.url and self.path == other.path
    
    def open(self) -> None:
        '''Open the downloaded item directory.'''
        try:
            os.startfile(self.path.replace(self.path.split('\\')[-1], ''))
        except:
            pass
class History(Item):
    '''Simulates a history item.'''
    def __init__(self,
        url: str,
        title: str,
        visit_count: int,
        last_visit: int,
        ts_epoch: int,
        browser: str,
    ):
        '''Initialize the History instance.'''
        super().__init__(ts_epoch, browser)
        self.url = url
        self.title = title
        self.visit_count = visit_count
        self.last_visit = self.to_datetime(last_visit)
        
    def __eq__(self, other: object) -> bool:
        '''Compare the history item with another history item.'''
        return self.url == other.url and self.title == other.title

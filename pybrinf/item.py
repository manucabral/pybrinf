import os

'''
This module contains the Item class.
The Item class is used to store different types of items (Downloads, History, etc).
Docstrings are written in Google style.
'''

class Item:
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

class Downloaded(Item):
    '''Simulates a downloaded item.'''
    def __init__(self,
        bytes: int,
        path: str,
        start: int,
        end: int,
        tab_url: str, 
        url: str
    ):
        self.bytes = bytes
        self.start_time = start
        self.end_time = end
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
        last_visit: int
    ):
        self.url = url
        self.title = title
        self.visit_count = visit_count
        self.last_visit = last_visit
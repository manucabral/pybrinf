
'''
This module contains the Item class.
The Item class is used to store different types of items (Downloads, History, etc).
Docstrings are written in Google style.
TODO: Add support for other types of items.
TODO: Add main class.
'''

class DownloadedItem:
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
    
    def __str__(self):
        '''Get the string representation of the object.'''
        return str(self.__class__)
    
    def __repr__(self):
        '''Get the string representation of the object.'''
        return self.__str__()

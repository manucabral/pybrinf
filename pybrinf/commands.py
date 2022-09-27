'''
    Commands implementation for PyBrinf.
    This module contains all command types supported and the Command classes for parsing SNSS files.
    Docstrings are written in Google style.
'''

import io
import enum
from pybrinf.reader import Reader

class MetaEnum(enum.EnumMeta):
    '''This class is used for creating an enum with a custom __contains__ method'''

    def __contains__(cls, item: int) -> bool:
        '''Check if the item is in the enum'''
        return item in cls._value2member_map_

class CommandType(enum.Enum, metaclass=MetaEnum):
    '''
        Enum for SNSS command types
        For now only UpdateTabNavigation is supported
    '''
    UpdateTabNavigation = 6

class Command:
    '''Command class core.'''

    def __init__(self, _id: int, content: bytes):
        '''
        Initialize the Command instance

        Args:
            id (int): The command id
            content (bytes): The command content
        '''
        self.id = _id
        self.content = content

    def __str__(self) -> str:
        '''Get the string representation of the command'''
        return __class__.__name__ + f'(id={self.id})'

    def __repr__(self) -> str:
        '''Get the representation of the command'''
        return self.__str__()

class CommandTabNavigation(Command):
    '''Command class for UpdateTabNavigation'''

    def __init__(self, _id: int, content: bytes):
        '''
        Initialize the CommandTabNavigation instance

        Args:
            id (int): The command id
            content (bytes): The command content
        '''
        super().__init__(_id, content)
        self.content = io.BytesIO(content)
        self.payload_size = Reader.uInt32(self.content)
        self.tab_id = Reader.uInt32(self.content)
        self.index = Reader.uInt32(self.content)
        self.url_len = Reader.uInt32(self.content)
        self.url = self.content.read(self.url_len).decode('utf-8')

    def __str__(self) -> str:
        '''Get the string representation of the command'''
        return __class__.__name__ + f'(id={self.id})'

    def __repr__(self) -> str:
        '''Get the string representation of the command'''
        return self.__str__()

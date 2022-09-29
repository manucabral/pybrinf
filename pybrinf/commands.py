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
        Source:
        https://source.chromium.org/chromium/chromium/src/+/main:components/sessions/core/session_service_commands.cc
    '''
    UpdateTabNavigation = 6
    SetSelectedNavigationIndex = 7
    SetSelectedTabInIndex = 8
    SetPinnedState = 12
    TabClosed = 16

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
        self.url = Reader.string(self.content)
        self.title = Reader.string16(self.content)

    def __str__(self) -> str:
        '''Get the string representation of the command'''
        return __class__.__name__ + f'(id={self.id})'

    def __repr__(self) -> str:
        '''Get the string representation of the command'''
        return self.__str__()

class SetSelectedNavigationIndex(Command):
    '''Command class for SetSelectedNavigationIndex'''

    def __init__(self, _id: int, content: bytes):
        '''
        Initialize the SetSelectedNavigationIndex instance

        Args:
            id (int): The command id
            content (bytes): The command content
        '''
        super().__init__(_id, content)
        self.content = io.BytesIO(content)
        self.tab_id = Reader.uInt32(self.content)
        self.index = Reader.uInt32(self.content)

    def __str__(self) -> str:
        '''Get the string representation of the command'''
        return __class__.__name__ + f'(id={self.id})'

    def __repr__(self) -> str:
        '''Get the string representation of the command'''
        return self.__str__()

class SetSelectedTabInIndex(Command):
    '''Command class for SetSelectedTabInIndex'''

    def __init__(self, _id: int, content: bytes):
        '''
        Initialize the SetSelectedTabInIndex instance

        Args:
            id (int): The command id
            content (bytes): The command content
        '''
        super().__init__(_id, content)
        self.content = io.BytesIO(content)
        self.index = Reader.uInt32(self.content)

    def __str__(self) -> str:
        '''Get the string representation of the command'''
        return __class__.__name__ + f'(id={self.id})'

    def __repr__(self) -> str:
        '''Get the string representation of the command'''
        return self.__str__()

class SetPinnedState(Command):
    '''Command class for SetPinnedState'''

    def __init__(self, _id: int, content: bytes):
        '''
        Initialize the SetPinnedState instance

        Args:
            id (int): The command id
            content (bytes): The command content
        '''
        super().__init__(_id, content)
        self.content = io.BytesIO(content)
        self.tab_id = Reader.uInt32(self.content)
        self.pinned = Reader.uInt32(self.content)

    def __str__(self) -> str:
        '''Get the string representation of the command'''
        return __class__.__name__ + f'(id={self.id})'

    def __repr__(self) -> str:
        '''Get the string representation of the command'''
        return self.__str__()


class TabClosed(Command):
    '''Command class for TabClosed'''

    def __init__(self, _id: int, content: bytes):
        '''
        Initialize the TabClosed instance

        Args:
            id (int): The command id
            content (bytes): The command content
        '''
        super().__init__(_id, content)
        self.content = io.BytesIO(content)
        self.tab_id = Reader.uInt32(self.content)

    def __str__(self) -> str:
        '''Get the string representation of the command'''
        return __class__.__name__ + f'(id={self.id})'

    def __repr__(self) -> str:
        '''Get the string representation of the command'''
        return self.__str__()

'''This module contains all the exceptions used in PyBrinf.'''

class SystemBrinfError(Exception):
    '''The exception is raised when a system error occurs.'''
    def __init__(self, error: str):
        super().__init__(error)
class BrinfError(Exception):
    '''This exception is raised when a error occurs in the Brinf module.'''
    def __init__(self, error: str):
        super().__init__(error)

class DatabaseError(Exception):
    '''This exception is raised when a error occurs in the database module.'''
    def __init__(self, error: str):
        super().__init__(error)

class BrowserError(Exception):
    '''This exception is raised when a error occurs from the browser.'''
    def __init__(self, error: str):
        super().__init__(error)

class SessionError(Exception):
    '''This exception is raised when a session error occurs.'''
    def __init__(self, error: str):
        super().__init__(error)

class ParserError(Exception):
    '''This exception is raised when the parser fails.'''
    def __init__(self, error: str):
        super().__init__(error)
'''This module contains all the exceptions used in PyBrinf.'''

class SystemBrinfError(Exception):
    '''Raise when a system error occurs.'''
class BrinfError(Exception):
    '''Raise when a error occurs in the Brinf module.'''

class DatabaseError(Exception):
    '''Raise when a error occurs in the database module.'''

class BrowserError(Exception):
    '''Raise when a error occurs from the browser.'''

class SessionError(Exception):
    '''Raise when a session error occurs.'''

class ParserError(Exception):
    '''Raise when the parser fails.'''

class FileError(Exception):
    '''Raise then the file handling and managements fails'''

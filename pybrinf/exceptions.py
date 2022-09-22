'''This module contains all the exceptions used in PyBrinf.'''

class BrinfNotInitialized(Exception):
    '''This exception is raised when the Brinf class is not initialized.'''
    def __init__(self):
        super().__init__('Brinf is not initialized. Please call the init method.')

class BrowserNotDetected(Exception):
    '''This exception is raised when the browser is not detected.'''
    def __init__(self):
        super().__init__('The browser could not be detected.')

class BrowserNotFound(Exception):
    '''This exception is raised when the browser is not found.'''
    def __init__(self):
        super().__init__('The browser could not be found.')
class InvalidBrowser(Exception):
    '''This exception is raised when the browser is invalid.'''
    def __init__(self):
        super().__init__('The browser instance is invalid.')

class BrowserNotInstalled(Exception):
    '''This exception is raised when the browser is not installed.'''
    def __init__(self):
        super().__init__('The browser is not installed.')

class FailedToConnect(Exception):
    '''This exception is raised when the database could not be connected.'''
    def __init__(self):
        super().__init__('The database could not be connected.')

class DatabaseIsNotConnected(Exception):
    '''This exception is raised when the database is not connected.'''
    def __init__(self):
        super().__init__('The database is not connected.')
class DatabaseIsConnected(Exception):
    '''This exception is raised when the database is already connected.'''
    def __init__(self):
        super().__init__('The database is already open.')

class FailedToCopyDatabase(Exception):
    '''This exception is raised when the database could not be copied.'''
    def __init__(self):
        super().__init__('Failed to copy the database.')

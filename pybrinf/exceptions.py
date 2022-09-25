'''This module contains all the exceptions used in PyBrinf.'''

class SystemNotSupported(Exception):
    '''The system is not supported.'''
    def __init__(self, system: str):
        '''Initialize the exception.'''
        super().__init__(f'The system {system} is not supported. Sorry.')

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
class BrowserNotSupported(Exception):
    '''This exception is raised when the browser is not supported.'''
    def __init__(self, browser: str):
        super().__init__(f'The browser {browser} is not supported. Please check the propertie supported_browsers.')

class BrowserNotInstalled(Exception):
    '''This exception is raised when the browser is not installed.'''
    def __init__(self):
        super().__init__('The browser is not installed.')

class BrowserNotRunning(Exception):
    '''This exception is raised when the browser is not running.'''
    def __init__(self):
        super().__init__('The browser is not running.')
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
    def __init__(self, error: str):
        super().__init__(f'Failed to copy the database: {error}')

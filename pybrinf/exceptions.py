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
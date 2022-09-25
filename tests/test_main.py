import unittest
from datetime import datetime
from pybrinf.__main__ import Brinf
from pybrinf.browser import Browser
from pybrinf.exceptions import BrowserNotFound, BrinfNotInitialized
from pybrinf.item import History, Downloaded

'''All tests for Brinf module.'''

class TestBrinf(unittest.TestCase):

    def setUp(self):
        self.brinf = Brinf()
        self.brinf.init()

    def test_get_browser(self):
        '''> Should return a Browser object.'''
        browser = self.brinf.browser('chrome')
        self.assertEqual(browser.installed, True)
        self.assertIsInstance(browser, Browser)
        self.assertIsInstance(browser.name, str)
        self.assertEqual(browser.name, 'Chrome')

    def test_get_default_browser(self):
        '''> Should return a Browser object.'''
        browser = self.brinf.default_browser
        self.assertEqual(browser.installed, True)
        self.assertIsInstance(browser, Browser)

    def test_get_default_browser_no_init(self):
        '''> Should raise a BrinfNotInitialized exception.'''
        self.brinf.reset()
        with self.assertRaises(BrinfNotInitialized):
            self.brinf.default_browser
    
    def test_get_invalid_browser(self):
        '''> Should raise a BrowserNotFound exception.'''
        with self.assertRaises(BrowserNotFound):
            self.brinf.browser('chrofox')
    
    def test_get_installed_browsers(self):
        '''> Should return a list of Browser objects.'''
        browsers = self.brinf.installed_browsers()
        self.assertIsInstance(browsers, list)
        for browser in browsers:
            self.assertIsInstance(browser, Browser)
            self.assertEqual(browser.installed, True)
    
    def test_get_installed_browsers_no_init(self):
        '''> Should raise a BrinfNotInitialized exception.'''
        self.brinf.reset()
        with self.assertRaises(BrinfNotInitialized):
            self.brinf.installed_browsers()
    
    def test_supported_browsers(self):
        '''> Should return a list of supported browsers in string format.'''
        browsers = self.brinf.supported_browsers
        self.assertIsInstance(browsers, list)
        self.assertIsInstance(browsers[0], str)
    
    def test_get_history(self):
        '''> Should return a list of History objects.'''
        browsers = self.brinf.installed_browsers()
        history = self.brinf.history(limit=3)
        self.assertIsInstance(history, list)
        self.assertEqual(len(history), 3 * len(browsers))

    def test_get_history_no_init(self):
        '''> Should raise a BrinfNotInitialized exception.'''
        self.brinf.reset()
        with self.assertRaises(BrinfNotInitialized):
            self.brinf.history()
    
    def test_get_downloads(self):
        '''> Should return a list of Downloaded objects.'''
        browsers = self.brinf.installed_browsers()
        downloads = self.brinf.downloads(limit=3)
        self.assertIsInstance(downloads, list)
        self.assertIsInstance(downloads[0], Downloaded)
    
    

if __name__ == '__main__':
    unittest.main()
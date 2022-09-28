import unittest
from pybrinf.__main__ import Brinf
from pybrinf.browser import Browser
from pybrinf.session import Session
from pybrinf.item import History, Downloaded
from pybrinf.exceptions import BrowserError

'''All tests for Browser module.'''

class TestBrowser(unittest.TestCase):

    def setUp(self):
        '''Using a basic browser.'''
        self.brinf = Brinf()
        self.brinf.init()
        self.browser = self.brinf.browser('chrome')
    
    def test_get_browser_name(self):
        '''> Should return the browser name.'''
        self.assertEqual(self.browser.name, 'Chrome')
    
    def test_get_browser_installed(self):
        '''> Should return the browser installed status.'''
        self.assertEqual(self.browser.installed, True)
    
    def test_get_browser_not_supported(self):
        '''> Should raise a BrowserError exception.'''
        with self.assertRaises(BrowserError):
            self.brinf.browser('chrofox')
    
    def test_get_browser_not_installed(self):
        '''> Should raise a BrowserError exception.'''
        # Using another browser only in this test.
        browser = self.brinf.browser('firefox')
        browser.set_app_path('C:\\Program Files\\Testasd')
        with self.assertRaises(BrowserError):
            browser.installed

    def test_get_browser_running(self):
        '''> Should return the browser running status.'''
        running = self.browser.running
        self.assertIsInstance(running, bool)

    def test_get_browser_version(self):
        '''> Should return the browser version.'''
        self.assertIsInstance(self.browser.version, str)
    
    def test_get_browser_path(self):
        '''> Should return the browser path.'''
        self.assertIsInstance(self.browser.path, str)
    
    def test_get_browser_app_path(self):
        '''> Should return the browser application path.'''
        self.assertIsInstance(self.browser.app_path, str)
    
    def test_get_browser_fullname(self):
        '''> Should return the browser full name.'''
        self.assertIsInstance(self.browser.fullname, str)
    
    def test_close_browser(self):
        '''> Should close the browser if it is running.'''
        if self.browser.running:
            self.browser.close()
        running = self.browser.running
        self.assertEqual(running, False)

    def test_get_browser_session(self):
        '''> Should return a Session object.'''
        session = self.browser.session()
        self.assertIsInstance(session, Session)
    
    def test_get_browser_history(self):
        '''> Should return a list of History objects.'''
        browser = self.brinf.browser('yandex')
        history = browser.history(limit=2)
        self.assertIsInstance(history, list)
        self.assertIsInstance(history[0], History)
        self.assertEqual(len(history), 2)
    
    def test_get_browser_downloads(self):
        '''> Should return a list of Download objects.'''
        # Using a browser what has downloads.
        browser = self.brinf.browser('yandex')
        downloads = browser.downloads(limit=2)
        self.assertIsInstance(downloads, list)
        self.assertIsInstance(downloads[0], Downloaded)
        self.assertEqual(len(downloads), 2)

if __name__ == '__main__':
    unittest.main()
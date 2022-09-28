import unittest
from pybrinf.__main__ import Brinf
from pybrinf.session import Session
from pybrinf.commands import CommandTabNavigation

'''All tests for Browser Session module.'''

class TestSession(unittest.TestCase):

    def setUp(self):
        '''Using a basic browser.'''
        self.brinf = Brinf()
        self.brinf.init()
        self.browser = self.brinf.browser('chrome')
        self.session = self.browser.session()
    
    def test_get_filename(self):
        '''> Should return the session filename.'''
        self.assertIsInstance(self.session.filename, str)
    
    def test_get_tabs(self):
        '''> Should return the session tabs.'''
        tabs = self.session.tabs()
        self.assertIsInstance(tabs, list)
        self.assertIsInstance(tabs[0], CommandTabNavigation)
    
    def test_get_current_tab(self):
        '''> Should return the current session tab.'''
        tab = self.session.current_tab()
        self.assertIsInstance(tab, CommandTabNavigation)
    
if __name__ == '__main__':
    unittest.main()
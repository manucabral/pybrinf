import unittest
from datetime import datetime
from pybrinf.utilities import Utilities

'''All tests for Utilities module.'''

class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.utilities = Utilities()
    
    def test_get_browser_data(self):
        '''> Should return a dict with the browser data.'''
        browser = self.utilities.get_browser_data('chrome')
        self.assertIsInstance(browser, dict)
    
    def test_get_website_query(self):
        '''> Should append the limit and offset to the query.'''
        query = self.utilities.website_query(True, limit=10, offset=0)
        self.assertIn('LIMIT 10', query)
        self.assertIn('OFFSET 0', query)
    
    def test_get_download_query(self):
        '''> Should append the limit and offset to the query.'''
        query = self.utilities.download_query(True, limit=10, offset=0)
        self.assertIn('LIMIT 10', query)
        self.assertIn('OFFSET 0', query)
    
    def test_date_to_int(self):
        '''> Should return the int representation of the date.'''
        date = self.utilities.date_to_int(datetime.now())
        self.assertIsInstance(date, int)
    
    def test_wrong_date_to_int(self):
        '''> Should raise a AttributeError because the date is not a datetime object.'''
        with self.assertRaises(AttributeError):
            self.utilities.date_to_int('no a datetime')

if __name__ == '__main__':
    unittest.main()
    
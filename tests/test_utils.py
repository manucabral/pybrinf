import unittest
from datetime import datetime
from pybrinf.utilities import Utilities

'''All tests for Utilities module.'''

class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.utilities = Utilities()
    
    def test_get_browser(self):
        '''Test the get_browser method.'''
        browser = self.utilities.get_browser_data('chrome')
        self.assertIsInstance(browser, dict)
    
    def test_website_query(self):
        '''Test the website_query method with filters.'''
        query = self.utilities.website_query(True, limit=10, offset=0)
        self.assertIn('LIMIT 10', query)
        self.assertIn('OFFSET 0', query)
    
    def test_download_query(self):
        '''Test the download_query method with filters.'''
        query = self.utilities.download_query(True, limit=10, offset=0)
        self.assertIn('LIMIT 10', query)
        self.assertIn('OFFSET 0', query)
    
    def test_date_to_int(self):
        '''Test the date_to_int method.'''
        date = self.utilities.date_to_int(datetime.now())
        self.assertIsInstance(date, int)
    
    def test_wrong_date_to_int(self):
        '''Test the date_to_int method with a wrong date.'''
        with self.assertRaises(AttributeError):
            self.utilities.date_to_int('no a datetime')


if __name__ == '__main__':
    unittest.main()
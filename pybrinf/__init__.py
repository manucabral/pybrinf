'''
    pybrinf - Python Browser Information.
    A simple way to get information about the browser and more.
'''

__title__ = 'pybrinf'
__version__ = '0.0.1'
__author__ = 'Manuel Cabral'
__license__ = 'GNU General Public License v3.0'

from pybrinf.__main__ import Brinf
from pybrinf.browser import Browser
from pybrinf.utilities import Utilities

__all__ = ['Brinf', 'Browser', 'Utilities']
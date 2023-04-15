'''
Register implementation for PyBrinf.
This module uses winreg to read the registry.
Docstrings are written in Google style.
'''

from pybrinf.exceptions import BrinfError
from pybrinf.utilities import Utilities

if Utilities.system() == 'win32':
    import winreg
else:
    raise BrinfError('This module is only compatible with Windows') from None

class Register:
    '''Register class core'''

    def openkey(self, key: str, sub: str, access: int = winreg.KEY_ALL_ACCESS) -> winreg.HKEYType:
        '''
        Open a registry key.

        Args:
            key (str): The key to open.
            sub (str): The subkey to open.
            access (int): The access to the key. Defaults to winreg.KEY_ALL_ACCESS.
        Raises:
            FileNotFoundError: The key does not exist.
            PermissionError: The access is denied.
            Exception: An unknown error occurred.
        Returns:
            winreg.HKEYType: The opened key.
        '''
        try:
            return winreg.OpenKey(key, sub, 0, access)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f'Key {sub} not found') from exc
        except PermissionError as exc:
            raise PermissionError('Access denied') from exc

    def extract(self, key: winreg.HKEYType, value: str) -> str:
        '''
        Extract a value from a registry key.

        Args:
            key (winreg.HKEYType): The key to extract the value from.
            value (str): The value to extract.
        Raises:
            FileNotFoundError: The value does not exist.
            Exception: An unknown error occurred.
        Returns:
            str: The extracted value.
        '''
        try:
            return winreg.QueryValueEx(key, value)[0]
        except FileNotFoundError as exc:
            raise FileNotFoundError(f'Value {value} not found') from exc
        except Exception as exc:
            raise Exception(f'An unknown error occurred: {exc}') from exc

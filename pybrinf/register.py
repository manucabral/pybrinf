import winreg

'''
    Register implementation for PyBrinf
    This module uses winreg to read the registry.
    Docstrings are written in Google style.
'''

class Register:
    '''Register class core'''

    def openkey(self, key: str, subkey: str, access: int = winreg.KEY_ALL_ACCESS) -> winreg.HKEYType:
        '''
        Open a registry key.

        Args:
            key (str): The key to open.
            subkey (str): The subkey to open.
            access (int): The access to the key. Defaults to winreg.KEY_ALL_ACCESS.

        Raises:
            FileNotFoundError: The key does not exist.
            PermissionError: The access is denied.
            Exception: An unknown error occurred.
        
        Returns:
            winreg.HKEYType: The opened key.
        '''
        try:
            return winreg.OpenKey(key, subkey, 0, access)
        except FileNotFoundError:
            raise FileNotFoundError('The key or subkey does not exist.')
        except PermissionError:
            raise PermissionError('You do not have permission to access this key.')
        except Exception as e:
            raise e
        
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
        except FileNotFoundError:
            raise FileNotFoundError('The value does not exist.')
        except Exception as e:
            raise e
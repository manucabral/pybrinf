import winreg

class Register:
    '''
    Register class, used to read and write to the windows registry.
    '''

    def openkey(self, key: str, subkey: str, access: int = winreg.KEY_ALL_ACCESS) -> winreg.HKEYType:
        '''
        Open a registry key.

        params:
            key: The key to open.
            subkey: The subkey to open.
            access: The access mode to use. Default is KEY_ALL_ACCESS.
                Note: If you change it may cause errors on some functions.
        returns:
            The opened key.
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

        params:
            key: The key to extract from.
            value: The value to extract.
        returns:
            The extracted value.
        '''
        try:
            return winreg.QueryValueEx(key, value)[0]
        except FileNotFoundError:
            raise FileNotFoundError('The value does not exist.')
        except Exception as e:
            raise e
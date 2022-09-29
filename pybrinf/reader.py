'''
    Reader implementation for PyBrinf.
    This module contains a class for reading bytes from a stream.
    Docstrings are written in Google style.
'''
import struct
import _io

class Reader:
    '''Reader class core.'''
    __endianess = '<' # Little endian

    @staticmethod
    def uInt32(stream: _io.BufferedReader) -> int:
        '''
        Read a 32-bit unsigned integer

        Args:
            stream (_io.BufferedReader): The stream to read from
        Returns:
            int: The read 16-bit unsigned integer
        '''
        return struct.unpack(Reader.__endianess + 'I', stream.read(4))[0]

    @staticmethod
    def uInt16(stream: _io.BufferedReader) -> int:
        '''
        Read a 16-bit unsigned integer

        Args:
            stream (_io.BufferedReader): The stream to read from
        Returns:
            int: The read 16-bit unsigned integer
        '''
        return struct.unpack(Reader.__endianess + 'H', stream.read(2))[0]

    @staticmethod
    def uInt8(stream: _io.BufferedReader) -> int:
        '''
        Read a 8-bit unsigned integer

        Args:
            stream (_io.BufferedReader): The stream to read from
        Returns:
            int: The read integer
        '''
        return struct.unpack(Reader.__endianess + 'B', stream.read(1))[0]

    @staticmethod
    def string(stream: _io.BufferedReader) -> str:
        '''
        Read a string

        Args:
            stream (_io.BufferedReader): The stream to read from
        Returns:
            str: The read string
        '''
        length = Reader.uInt32(stream)
        return stream.read(length).decode('utf-8', errors='ignore')

    @staticmethod
    def string16(stream: _io.BufferedReader) -> str:
        '''
        Read a string with 16-bit length
        Source: lemnos/chrome-session-dump
        TODO: Finish this :p

        Args:
            stream (_io.BufferedReader): The stream to read from
        Returns:
            str: The read string
        '''
        length = Reader.uInt32(stream) * 2
        if length % 4 != 0:
            length += 4 - (length % 4)
            return stream.read(length).decode('utf-8', errors='ignore')
        return 'undefined'

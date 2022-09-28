'''
    Parser implementation for PyBrinf.
    This module contains the parser for SNSS files.
    Docstrings are written in Google style.
'''

import os
import _io

from pybrinf.reader import Reader
from pybrinf.exceptions import ParserError
from pybrinf.commands import CommandType, Command, CommandTabNavigation, SetSelectedNavigationIndex

class Parser:
    '''Parser class core.'''
    __signature = 0x53534E53 # b'SNSS'

    def __init__(self, file: str):
        '''
        Initialize the Parser instance

        Args:
            file (str): The file to parse
        '''
        self.__file = file

    def __open(self) -> _io.BufferedReader:
        '''
        Open a file

        Raises:
            ParserError: If the file is not found
        Returns:
            _io.BufferedReader: The opened file
        '''
        try:
            return open(self.__file, 'rb')
        except FileNotFoundError as exc:
            raise ParserError(f'File {self.__file} not found') from exc

    def __close(self, file: _io.BufferedReader):
        '''
        Close the file

        Args:
            file (_io.BufferedReader): The file to close
        returns:
            None
        '''
        file.close()

    def __size(self, stream: _io.BufferedReader) -> int:
        '''
        Get the stream size

        Args:
            stream (_io.BufferedReader): The stream to get the size from
        Returns:
            int: The stream size.
        '''
        stream.seek(0, os.SEEK_END)
        end = stream.tell()
        stream.seek(0, os.SEEK_SET)
        return end

    def __identify_command(self, command_id: int, command_content: bytes) -> Command:
        '''
        Identify the command type from a command id
        NOTE: For now only UpdateTabNavigation is supported.
        TODO: Implement other command types support.

        Args:
            command_id (int): The command id
            command_content (bytes): The command content
        Returns:
            Command: A inherited class of Command class
        '''
        if command_id in CommandType:
            if command_id == CommandType.UpdateTabNavigation.value:
                return CommandTabNavigation(command_id, command_content)
            if command_id == CommandType.SetSelectedNavigationIndex.value:
                return SetSelectedNavigationIndex(command_id, command_content)
            return Command(command_id, command_content)
        return None

    def filter_command(self, commands: list, command_id: int) -> list[Command]:
        '''
        Filter commands by id

        Args:
            commands (list): The commands to filter
            command_id (int): The command id to filter by
        Returns:
            list: The filtered commands
        '''
        return [command for command in commands if command.id == command_id]

    @property
    def commands(self) -> list[Command]:
        '''
        Get all commands from a SNSS file

        Raises:
            ParserError: If the file is not a SNSS file or the file is corrupted
        Returns:
            list: A list of Command instances
        '''
        commands = []
        stream = self.__open()
        file_size = self.__size(stream)
        signature = Reader.uInt32(stream)
        _ = Reader.uInt32(stream) # Version, not used.
        if signature != self.__signature:
            self.__close(stream)
            raise ParserError('Invalid SNSS file. Signature does not match')
        while file_size - stream.tell() > 0:
            command_size = Reader.uInt16(stream)
            if command_size == 0:
                raise ParserError('Invalid command size, maybe corrupted file')
            command_id = Reader.uInt8(stream)
            command_content = stream.read(command_size - 1)
            command = self.__identify_command(command_id, command_content)
            if command:
                commands.append(command)
        self.__close(stream)
        return commands

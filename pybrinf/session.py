'''
    Browser session implementation for PyBrinf.
    This module is used to get session information of a browser.
    Docstrings are written in Google style.
'''

import os

from pybrinf.parser import Parser
from pybrinf.exceptions import SessionError
from pybrinf.item import Tab
from pybrinf.commands import CommandType

class Session:
    '''Session class core.'''

    def __init__(self, path: str, browser: str):
        '''
        Initialize the Session instance.

        Args:
            path (str): The path of the Session folder.
        Raises:
            SessionError: If the path is not a valid Session folder.
        '''
        self.__path = path + '\\Sessions'
        self.browser = browser
        if not self.__exists:
            raise SessionError('Sessions folder not found')

    @property
    def __exists(self) -> bool:
        '''
        Check if the Sessions path exists

        Returns:
            bool: True if the Sessions path exists, False otherwise.
        '''
        return os.path.exists(self.__path)

    @property
    def __last(self) -> str:
        '''
        Get the last Session file

        Raises:
            SessionError: If the Sessions folder is empty.
        Returns:
            str: The last Session file.
        '''
        files = os.listdir(self.__path)
        sessions = [file.split('_') for file in files if file.startswith('Session')]
        if not sessions:
            raise SessionError('No Session files found')
        sessions = sorted(sessions, key=lambda x: x[1], reverse=True)
        return '_'.join(sessions[0])

    @property
    def filename(self) -> str:
        '''
        Get the session filename

        Returns:
            str: The session filename.
        '''
        return self.__last

    def __parse_tabs(self, *args) -> list[Tab]:
        '''
        Parse the tab from the UpdateTabNavigation commands and return a list of Tab objects.
        More friendly to use than the CommandTabNavigation object.

        Args:
            tab_navigations (list[UpdateTabNavigation]): UpdateTabNavigation commands.
            pinned_states (list[SetPinnedState]): SetPinnedState commands.
            selected_tab (SetSelectedNavigationIndex): SetSelectedNavigationIndex command.
        Returns:
            Tab: The parsed tabs.
        '''
        tabs = []
        tab_navigations = args[0]
        pinned_states = args[1]
        selected_tab = args[2]
        for command in tab_navigations:
            tab = Tab(self.browser, command.tab_id, command.index, command.url, command.title)
            for pinned_state in pinned_states:
                tab.pinned = pinned_state.tab_id == command.tab_id
            tab.active = tab.id == selected_tab.tab_id
            tabs.append(tab)
        return tabs

    def __remove_repeated_tabs(self, tabs: list[Tab]) -> list[Tab]:
        '''
        Remove repeated tabs from the list of tabs

        Args:
            tabs (list[Tab]): The tabs to remove the repeated tabs.

        Returns:
            list[Tab]: The tabs without repeated tabs.
        '''
        new_tabs = []
        for tab in tabs:
            if tab.id not in [new_tab.id for new_tab in new_tabs]:
                new_tabs.append(tab)
        return new_tabs

    def tabs(self) -> list[Tab]:
        '''
        Get all tabs from the last Session file

        Returns:
            list[CommandTabNavigation]: All updated tabs from the last Session file.
        '''
        file_path = os.path.join(self.__path, self.__last)
        parser = Parser(file_path)
        commands = parser.commands
        tab_navs = parser.filter_command(commands, CommandType.UpdateTabNavigation.value)
        pinned_states = parser.filter_command(commands, CommandType.SetPinnedState.value)
        selected_nav = parser.filter_command(commands, CommandType.SetSelectedNavigationIndex.value)
        tabs = self.__parse_tabs(tab_navs, pinned_states, selected_nav[-1])
        return self.__remove_repeated_tabs(tabs)

    @property
    def current_tab(self) -> Tab:
        '''
        Get the current tab from the last Session file

        Returns:
            Tab: The current tab from the last Session file.
        '''
        return [tab for tab in self.tabs() if tab.active][0]

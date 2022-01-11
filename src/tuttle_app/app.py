"""
Painless business planning for freelancers
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import pandas
import numpy
import sqlmodel
import pyicloud


class Tuttle(toga.App):

    def dummy_command(self, widget):
        """A dummy command for demo purposes"""
        df = pandas.DataFrame()
        print("Command triggered")

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        # Main window
        main_box = toga.Box()
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box

        ## Commands
        menu_file = toga.Group("File")  
        menu_view = toga.Group("View")
        
        cmd_example_file = toga.Command(
            self.dummy_command,
            label='Test',
            tooltip='Test command',
            group=menu_file
        )

        cmd_example_view = toga.Command(
            self.dummy_command,
            label='Test',
            tooltip='Test command',
            group=menu_view
        )

        commands = (
            cmd_example_view,
            cmd_example_file
        )
        self.app.commands.add(*commands)
        self.app.main_window.toolbar.add(*commands)

        self.main_window.show()


def main():
    return Tuttle()

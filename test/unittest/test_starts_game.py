from codebreaker_lib import codebreaker
from mockito import *

class TestStart(object):
    def setup(self):
        self.output = mock()

    def test_should_print_welcome_message(self):
        codebreaker(self.output)
        verify(self.output).write(contains("Welcome to Codebreaker!"))

    def test_should_start_game(self):
        codebreaker(self.output)
        verify(self.output).write(contains("Enter guess:"))
from codebreaker_lib import codebreaker
from mockito import *

# run nose with --testmatch=(?:\\b|_)([Tt]est|should) to pick up the should* tests
class TestStart(object):
    def setup(self):
        self.output = mock()

    def should_print_welcome_message(self):
        codebreaker(self.output)
        verify(self.output).write(contains("Welcome to Codebreaker!"))

    def should_prompt_for_the_first_guess(self):
        codebreaker(self.output)
        verify(self.output).write(contains("Enter guess:"))
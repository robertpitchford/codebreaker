from codebreaker_lib import codebreaker
from mockito import *

# run nose with --testmatch=(?:\\b|_)([Tt]est|should) to pick up the should* tests
class TestStartGame(object):
    def setup(self):
        self.output = mock()
        codebreaker(self.output)

    def should_print_welcome_message(self):
        verify(self.output).write(contains("Welcome to Codebreaker!"))

    def should_prompt_for_the_first_guess(self):
        verify(self.output).write(contains("Enter guess:"))

class TestSubmitGuess(object):
    def setup(self):
        self.output = mock()

    def should_return_empty_string_for_no_matches(self):
        cb = codebreaker(self.output)
        cb.guess("5555")
        verify(self.output).write("\n")
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
        self.cb = codebreaker(self.output)
        self.cb.start("1234")

    def should_return_correct_mark_no_matches(self):
        self.cb.guess("5555")
        verify(self.output).write("\n")

    def should_return_correct_mark_for_one_exact_match(self):
        self.cb.guess("1555")
        verify(self.output).write("+\n")

    def should_return_correct_mark_for_one_number_match(self):
        self.cb.guess("5155")
        verify(self.output).write("-\n")

    def should_return_correct_mark_for_all_exact_matches(self):
        self.cb.guess("1234")
        verify(self.output).write("++++\n")

    def should_return_correct_mark_for_one_number_match_with_duplicates(self):
        self.cb.guess("1111")
        verify(self.output).write("+\n")

class TestCorrectGuess(object):
    def setup(self):
        self.output = mock()
        self.cb = codebreaker(self.output)
        self.cb.start("1234")

    def should_return_true_for_correct_guess(self):
        CORRECT_GUESS = "1234"
        assert self.cb.guess(CORRECT_GUESS) == True

    def should_return_false_for_incorrect_guess(self):
        INCORRECT_GUESS = "4321"
        assert self.cb.guess(INCORRECT_GUESS) == False

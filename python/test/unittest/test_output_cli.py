import os
from mockito.matchers import contains
from mockito.mocking import mock
from mockito.mockito import verify
from output_cli import OutputCli

class TestOutputCli(object):
    def setup(self):
        self.output = mock()
        self.reporter = OutputCli(self.output)

    def should_print_welcome_message(self):
        self.reporter.report_welcome()
        verify(self.output).write(contains("Welcome to Codebreaker!"))

    def should_prompt_for_the_first_guess(self):
        self.reporter.report_welcome()
        verify(self.output).write(contains("Enter guess:"))

    def should_report_win_condition(self):
        self.reporter.report_win()
        verify(self.output).write(contains("Correct! You cracked the code"))

    def should_print_matches(self):
        self.reporter.report_matches("++++")
        verify(self.output).write(contains("++++" + os.linesep))

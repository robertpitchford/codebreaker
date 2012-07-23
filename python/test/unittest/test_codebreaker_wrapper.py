from mockito import *
from codebreaker_wrapper import codebreaker_wrapper

class TestCodebreakerWrapper(object):
    def test_generate_secret(self):
        w = codebreaker_wrapper(mock(), mock())
        w.randrange = lambda x: 2

        assert w.generate_secret() == "3456"

    def should_not_end_game_for_incorrect_guess(self):
        output, codebreaker = self.play_game("5555")

        assert codebreaker.isPlaying == True
        verify(output, never).report_win()

    def should_end_game_for_correct_guess(self):
        output, codebreaker = self.play_game("1234\n")

        assert codebreaker.isPlaying == False
        verify(output).report_win()

    def play_game(self, guess):
        input = mock()
        output = mock()
        when(input).readline().thenReturn(guess)
        w = codebreaker_wrapper(input, output)
        w.generate_secret = lambda: "1234"
        w.new_game()
        w.next_guess()
        return output, w

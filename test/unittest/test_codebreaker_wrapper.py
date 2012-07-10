from mockito import *
from codebreaker_wrapper import codebreaker_wrapper

class TestCodebreakerWrapper(object):
    def test_generate_secret(self):
        w = codebreaker_wrapper(mock(), mock())
        w.randrange = lambda x: 2

        assert w.generate_secret() == "3456"

    def should_not_end_game_for_incorrect_guess(self):
        input = mock()
        when(input).readline().thenReturn("5555\n")

        w = codebreaker_wrapper(input, mock())
        w.generate_secret = lambda: "1234"
        w.new_game()

        w.next_guess()

        assert w.isPlaying == True

    def should_end_game_for_correct_guess(self):
        input = mock()
        output = mock()
        when(input).readline().thenReturn("1234\n")

        w = codebreaker_wrapper(input, output)
        w.generate_secret = lambda: "1234"
        w.new_game()

        w.next_guess()

        assert w.isPlaying == False
        verify(output).write(contains("Correct! You cracked the code"))

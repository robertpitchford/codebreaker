#noinspection PyUnresolvedReferences
import test_helper
from mockito import *
from codebreaker_lib import codebreaker
from codebreaker_wrapper import codebreaker_wrapper

class State(object):
    pass

def reset_state():
    global state
    state = State()

def codebreaker_is_not_running():
    pass

def I_start_a_new_game():
    reset_state()
    state.output = mock()
    input = mock()
    codebreaker_wrapper(input, state.output)

def I_should_see(expected):
    verify(state.output).write(contains(expected))

def I_should_not_see(expected):
    verify(state.output, never).write(contains(expected))

def the_secret_code(secret):
    reset_state()
    state.output = mock()
    state.cb = codebreaker(state.output)
    state.cb.start(secret)

def I_guess(guess):
    state.cb.guess(guess)

def the_mark_should_be(mark):
    verify(state.output).write(mark + "\n")

def codebreaker_is_started():
    reset_state()
    state.SECRET = "1234"
    state.input = mock()
    state.output = mock()
    state.wrapper = codebreaker_wrapper(state.input, state.output)
    state.wrapper.generate_secret = lambda: state.SECRET
    state.wrapper.new_game()

def I_guess_the_correct_code():
    when(state.input).readline().thenReturn(state.SECRET + "\n")
    state.wrapper.next_guess()

def I_guess_an_incorrect_code():
    when(state.input).readline().thenReturn("5555\n")
    state.wrapper.next_guess()

def the_game_should_end():
    assert state.wrapper.isPlaying == False

def the_game_should_not_end():
    assert state.wrapper.isPlaying == True
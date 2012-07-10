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

def the_secret_code(secret):
    reset_state()
    state.output = mock()
    state.cb = codebreaker(state.output)
    state.cb.start(secret)

def I_guess(guess):
    state.cb.guess(guess)

def the_mark_should_be(mark):
    verify(state.output).write(mark + "\n")

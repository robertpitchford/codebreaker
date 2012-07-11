#noinspection PyUnresolvedReferences
import test_helper
from mockito import *
from codebreaker_lib import codebreaker
from codebreaker_wrapper import codebreaker_wrapper
from lettuce import step

class State(object):
    pass

def reset_state():
    global state
    state = State()

@step(u'codebreaker is not running')
def given_codebreaker_is_not_running(step):
    pass

@step(u'I start a new game')
def when_i_start_a_new_game(step):
    reset_state()
    state.output = mock()
    input = mock()
    codebreaker_wrapper(input, state.output)

@step(u'I should see "([^"]*)"')
def then_i_should_see_msg(step, msg):
    verify(state.output).write(contains(msg))

@step(u'I should not see "([^"]*)"')
def I_should_not_see(step, msg):
    verify(state.output, never).write(contains(msg))

@step(u'the secret code "([^"]*)"')
def the_secret_code(step, secret):
    reset_state()
    state.output = mock()
    state.cb = codebreaker(state.output)
    state.cb.start(secret)

@step(u'I guess "([^"]*)"')
def I_guess(step, guess):
    state.cb.guess(guess)

@step(u'the mark should be "([^"]*)"')
def the_mark_should_be(step, mark):
    verify(state.output).write(mark + "\n")

@step(u'codebreaker is started')
def codebreaker_is_started(step):
    reset_state()
    state.SECRET = "1234"
    state.input = mock()
    state.output = mock()
    state.wrapper = codebreaker_wrapper(state.input, state.output)
    state.wrapper.generate_secret = lambda: state.SECRET
    state.wrapper.new_game()

@step(u'I guess the correct code')
def I_guess_the_correct_code(step):
    when(state.input).readline().thenReturn(state.SECRET + "\n")
    state.wrapper.next_guess()

@step(u'I guess an incorrect code')
def I_guess_an_incorrect_code(step):
    when(state.input).readline().thenReturn("5555\n")
    state.wrapper.next_guess()

@step(u'the game should end')
def the_game_should_end(step):
    assert state.wrapper.isPlaying == False

@step(u'the game should not end')
def the_game_should_not_end(step):
    assert state.wrapper.isPlaying == True
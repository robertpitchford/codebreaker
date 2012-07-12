##noinspection PyUnresolvedReferences
import test_helper
from behave import *
import mockito
import codebreaker_lib
import codebreaker_wrapper

class State(object):
    pass

def reset_state():
    global state
    state = State()

@given(u'codebreaker is not running')
def given_codebreaker_is_not_running(context):
    pass

@when(u'I start a new game')
def when_i_start_a_new_game(context):
    reset_state()
    state.output = mockito.mock()
    input = mockito.mock()
    codebreaker_wrapper.codebreaker_wrapper(input, state.output)

@then(u'I should see "{msg}"')
def then_i_should_see_msg(context, msg):
    mockito.verify(state.output).write(mockito.contains(msg))

@then(u'I should not see "{msg}"')
def I_should_not_see(context, msg):
    mockito.verify(state.output, mockito.never).write(mockito.contains(msg))

@given(u'the secret code "{secret}"')
def the_secret_code(context, secret):
    reset_state()
    state.output = mockito.mock()
    state.cb = codebreaker_lib.codebreaker(state.output)
    state.cb.start(secret)

@when(u'I guess "{guess}"')
def I_guess(context, guess):
    state.cb.guess(guess)

@then(u'the mark should be "{mark}"')
def the_mark_should_be_mark(context, mark):
    mockito.verify(state.output).write(mark + "\n")

@then(u'the mark should be ""')
def the_mark_should_be(context):
    the_mark_should_be_mark(context, "")

@given(u'codebreaker is started')
def codebreaker_is_started(context):
    reset_state()
    state.SECRET = "1234"
    state.input = mockito.mock()
    state.output = mockito.mock()
    state.wrapper = codebreaker_wrapper.codebreaker_wrapper(state.input, state.output)
    state.wrapper.generate_secret = lambda: state.SECRET
    state.wrapper.new_game()

@when(u'I guess the correct code')
def I_guess_the_correct_code(context):
    mockito.when(state.input).readline().thenReturn(state.SECRET + "\n")
    state.wrapper.next_guess()

@when(u'I guess an incorrect code')
def I_guess_an_incorrect_code(context):
    mockito.when(state.input).readline().thenReturn("5555\n")
    state.wrapper.next_guess()

@then(u'the game should end')
def the_game_should_end(context):
    assert state.wrapper.isPlaying == False

@then(u'the game should not end')
def the_game_should_not_end(context):
    assert state.wrapper.isPlaying == True
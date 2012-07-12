##noinspection PyUnresolvedReferences
import test_helper
from mockito import mock, verify, contains, never, when
import behave
import codebreaker_lib
import codebreaker_wrapper

@behave.given(u'codebreaker is not running')
def given_codebreaker_is_not_running(context):
    pass

@behave.when(u'I start a new game')
def when_i_start_a_new_game(context):
    context.output = mock()
    input = mock()
    codebreaker_wrapper.codebreaker_wrapper(input, context.output)

@behave.then(u'I should see "{msg}"')
def then_i_should_see_msg(context, msg):
    verify(context.output).write(contains(msg))

@behave.then(u'I should not see "{msg}"')
def I_should_not_see(context, msg):
    verify(context.output, never).write(contains(msg))

@behave.given(u'the secret code "{secret}"')
def the_secret_code(context, secret):
    context.output = mock()
    context.cb = codebreaker_lib.codebreaker(context.output)
    context.cb.start(secret)

@behave.when(u'I guess "{guess}"')
def I_guess(context, guess):
    context.cb.guess(guess)

@behave.then(u'the mark should be "{mark}"')
def the_mark_should_be_mark(context, mark):
    verify(context.output).write(mark + "\n")

@behave.then(u'the mark should be ""')
def the_mark_should_be(context):
    the_mark_should_be_mark(context, "")

@behave.given(u'codebreaker is started')
def codebreaker_is_started(context):
    context.SECRET = "1234"
    context.input = mock()
    context.output = mock()
    context.wrapper = codebreaker_wrapper.codebreaker_wrapper(context.input, context.output)
    context.wrapper.generate_secret = lambda: context.SECRET
    context.wrapper.new_game()

@behave.when(u'I guess the correct code')
def I_guess_the_correct_code(context):
    when(context.input).readline().thenReturn(context.SECRET + "\n")
    context.wrapper.next_guess()

@behave.when(u'I guess an incorrect code')
def I_guess_an_incorrect_code(context):
    when(context.input).readline().thenReturn("5555\n")
    context.wrapper.next_guess()

@behave.then(u'the game should end')
def the_game_should_end(context):
    assert context.wrapper.isPlaying == False

@behave.then(u'the game should not end')
def the_game_should_not_end(context):
    assert context.wrapper.isPlaying == True
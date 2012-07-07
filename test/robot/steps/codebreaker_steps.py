#noinspection PyUnresolvedReferences
import test_helper
from codebreaker_lib import codebreaker
from mockito import *

output = None
cb = None

def codebreaker_is_not_running():
    pass

def I_start_a_new_game():
    global output
    output = mock()
    codebreaker(output)

def I_should_see(expected):
    verify(output).write(contains(expected))

def the_secret_code(secret):
    global cb, output
    output = mock() # mock needs to be reset between calls
    cb = codebreaker(output)
    cb.start(secret)

def I_guess(guess):
    cb.guess(guess)

def the_mark_should_be(mark):
    verify(output).write(mark + "\n")

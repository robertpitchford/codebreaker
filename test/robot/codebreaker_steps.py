#noinspection PyUnresolvedReferences
import test_helper
from codebreaker_lib import codebreaker
from mockito import *

output = mock()

def codebreaker_is_not_running():
    pass

def I_start_a_new_game():
    cb = codebreaker(output)

def I_should_see(expected):
    verify(output).write(contains(expected))
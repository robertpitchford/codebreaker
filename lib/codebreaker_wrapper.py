import sys
from codebreaker_lib import codebreaker

class codebreaker_wrapper(object):
    def start(self, input, output, codebreakerWantsToPlay=True):
        cb = codebreaker(output)
        cb.start("1234")
        while codebreakerWantsToPlay:
            guess = input.readline()
            if cb.guess(guess):
                print "Correct! You cracked the code\n"
                return 0

    #TODO
    # method to create random secret
    # to test it, stub the random call with something predictable - we aren't testing random lib!!!
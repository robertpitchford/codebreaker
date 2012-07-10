import random
from codebreaker_lib import codebreaker

class codebreaker_wrapper(object):
    def start(self, input, output, codebreakerWantsToPlay=True):
        cb = codebreaker(output)
        cb.start(self.generate_secret())
        while codebreakerWantsToPlay:
            guess = input.readline()
            if cb.guess(guess):
                print "Correct! You cracked the code\n"
                return 0

    def generate_secret(self):
        choices = list("123456")
        secret = ""
        for _ in xrange(0, 4):
            r = self.randrange(len(choices))
            secret += choices[r]
            del choices[r]

        return secret

    def randrange(self, size):
        return random.randrange(size)
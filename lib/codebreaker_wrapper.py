import random
from codebreaker_lib import codebreaker

class codebreaker_wrapper(object):
    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.isPlaying=False

        self.cb = codebreaker(self.output)

    def new_game(self):
        self.isPlaying=True
        self.cb.start(self.generate_secret())

    def start(self):
        while self.isPlaying:
            self.next_guess()

    def next_guess(self):
        print "HELLO"
        guess = self.input.readline()
        print "guess: " + guess
        self.cb.guess(guess)
        if self.cb.has_won(guess):
            self.output.write("Correct! You cracked the code\n")
            self.isPlaying = False

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
from marker import Marker

class codebreaker(object):
    def __init__(self, output):
        self.output = output
        self.output.write("Welcome to Codebreaker!\n")
        self.output.write("Enter guess:\n")

    def start(self, secret):
        self.secret = secret
        self.marker = Marker(self.secret)

    def guess(self, guess):
        marks = "+" * self.marker.exact_match_count(guess) + "-" * self.marker.number_match_count(guess) + "\n"
        self.output.write(marks)

    def has_won(self, guess):
        return self.marker.exact_match_count(guess) == len(self.secret)
from marker import Marker

class codebreaker(object):
    def __init__(self, output):
        self.output = output
        self.output.write("Welcome to Codebreaker!\n")
        self.output.write("Enter guess:\n")

    def start(self, secret):
        self.secret = secret

    def guess(self, guess):
        marker = Marker(self.secret)
        marks = "+" * marker.exact_match_count(guess) + "-" * marker.number_match_count(guess) + "\n"
        self.output.write(marks)
        return marks == "++++\n"

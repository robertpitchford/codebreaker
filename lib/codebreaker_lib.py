class codebreaker(object):
    def __init__(self, output):
        self.output = output
        self.output.write("Welcome to Codebreaker!\n")
        self.output.write("Enter guess:\n")

    def start(self, secret):
        self.secret = secret

    def guess(self, guess):
        if guess[0] == self.secret[0]:
            self.output.write("+\n")
        elif guess[0] in self.secret:
            self.output.write("-\n")
        else:
            self.output.write("\n")
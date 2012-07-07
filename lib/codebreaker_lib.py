class codebreaker(object):
    def __init__(self, output):
        self.output = output
        self.output.write("Welcome to Codebreaker!\n")
        self.output.write("Enter guess:\n")

    def start(self, secret):
        self.secret = secret

    def guess(self, guess):
        marks = ""
        for i in range(0, 4):
            if guess[i] == self.secret[i]:
                marks += "+"
            elif guess[i] in self.secret:
                marks += "-"

        self.output.write(marks + "\n")
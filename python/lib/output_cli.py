import os

class OutputCli(object):
    def __init__(self, output):
        self.o = output

    def report_win(self):
        self.o.write("Correct! You cracked the code\n")

    def report_matches(self, marks):
        self.o.write(marks + os.linesep)

    def report_welcome(self):
        self.o.write("Welcome to Codebreaker!\n")
        self.o.write("Enter guess:\n")

import sys
sys.path.append("lib")

from codebreaker_lib import codebreaker

cb = codebreaker(sys.stdout)
cb.start("1234")
while True:
    guess = sys.stdin.readline()
    if cb.guess(guess):
        print "Correct! You cracked the code\n"
        sys.exit(0)
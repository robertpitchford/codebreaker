import sys
sys.path.append("lib")

from codebreaker_lib import codebreaker

cb = codebreaker(sys.stdout)
cb.start("1234")
while True:
    guess = sys.stdin.readline()
    cb.guess(guess)
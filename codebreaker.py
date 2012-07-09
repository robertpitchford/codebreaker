import sys
sys.path.append("lib")

from codebreaker_wrapper import codebreaker_wrapper

sys.exit(codebreaker_wrapper().start(sys.stdin, sys.stdout))


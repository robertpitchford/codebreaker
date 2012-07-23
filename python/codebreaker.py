import sys
sys.path.append("lib")

from codebreaker_wrapper import codebreaker_wrapper

sys.exit(codebreaker_wrapper().new_game().start())


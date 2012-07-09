class codebreaker(object):
    def __init__(self, output):
        self.output = output
        self.output.write("Welcome to Codebreaker!\n")
        self.output.write("Enter guess:\n")

    def start(self, secret):
        self.secret = secret

    def exact_match_count(self, guess):
        return reduce (lambda count, i: count + (1 if guess[i] == self.secret[i] else 0), range(0,4), 0)

    def number_match_count(self, guess):
        return self.total_match_count(guess) - self.exact_match_count(guess)

    def total_match_count(self, guess):
        secret = list(self.secret)
        return reduce(lambda count, g: count + (1 if self.delete_first(g, secret) else 0), guess, 0)

    def delete_first(self, g, secret):
        try:
            secret.remove(g)
            return True
        except Exception:
            return False


    def delete_char_at(self, pos, secret):
        return secret[:pos] + secret[pos + 1:]

    def is_number_match(self, guess, i):
        return guess[i] in self.secret

    def guess(self, guess):
        marks = "+" * self.exact_match_count(guess) + "-" * self.number_match_count(guess) + "\n"
        self.output.write(marks)
        return marks == "++++\n"

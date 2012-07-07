class codebreaker(object):
    def __init__(self, output):
        self.output = output
        self.output.write("Welcome to Codebreaker!\n")
        self.output.write("Enter guess:\n")

    def start(self, secret):
        self.secret = secret

    def exact_match_count(self, guess):
        count = 0
        for i in range(0, 4):
            if guess[i] == self.secret[i]:
                count += 1
        return count

    def number_match_count(self, guess):
        return self.total_match_count(guess) - self.exact_match_count(guess)

    def delete_char_at(self, pos, secret):
        return secret[:pos] + secret[pos + 1:]

    def total_match_count(self, guess):
        count = 0
        secret = self.secret
        for i in range(0, 4):
            pos = secret.find(guess[i])
            if pos != -1:
                secret = self.delete_char_at(pos, secret)
                count += 1
        return count

    def is_number_match(self, guess, i):
        return guess[i] in self.secret

    def guess(self, guess):
        self.output.write("+" * self.exact_match_count(guess) + "-" * self.number_match_count(guess) + "\n")

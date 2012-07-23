class Marker(object):
    def __init__(self, secret):
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

module Codebreaker
  class Marker
    def initialize(secret, guess)
      @secret = secret
      @guess = guess
    end

    def total_number_matches
      total_matches(:number_match?)
    end

    def total_exact_matches
      total_matches(:exact_match?)
    end

    def total_matches(method)
      (0..3).inject(0) do |count, index|
        count + (send(method, index) ? 1 : 0)
      end
    end

    def number_match?(index)
      @secret.include?(@guess[index]) && !exact_match?(index)
    end

    def exact_match?(index)
      @secret[index] == @guess[index]
    end
  end
end
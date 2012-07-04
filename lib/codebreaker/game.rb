module Codebreaker
  class Game
    def initialize(output)
      @output = output
    end

    def start(secret)
      @secret = secret
      @output.puts "Welcome to Codebreaker!"
      @output.puts "Enter guess:"
    end

    def guess(guess)
      @output.puts "+" * total_exact_matches(guess) + "-" * total_number_matches(guess)
    end

    def total_number_matches(guess)
      number_match_count = 0
      (0..3).each do |index|
        if number_match?(guess, index)
          number_match_count += 1
        end
      end
      number_match_count
    end

    def total_exact_matches(guess)
      exact_match_count = 0
      (0..3).each do |index|
        if exact_match?(guess, index)
          exact_match_count += 1
        end
      end
      exact_match_count
    end

    def number_match?(guess, index)
      @secret.include?(guess[index]) && !exact_match?(guess, index)
    end

    def exact_match?(guess, index)
      @secret[index] == guess[index]
    end
  end
end
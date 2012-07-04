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
      total_matches(guess, :number_match?)
    end

    def total_exact_matches(guess)
      total_matches(guess, :exact_match?)
    end

    def total_matches(guess, method)
      matches = 0
      (0..3).each do |index|
        if send(method, guess, index)
          matches += 1
        end
      end
      matches
    end

    def number_match?(guess, index)
      @secret.include?(guess[index]) && !exact_match?(guess, index)
    end

    def exact_match?(guess, index)
      @secret[index] == guess[index]
    end
  end
end
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
      (0..3).inject(0) do |count, index|
        count + (send(method, guess, index) ? 1 : 0)
      end
    end

    def number_match?(guess, index)
      @secret.include?(guess[index]) && !exact_match?(guess, index)
    end

    def exact_match?(guess, index)
      @secret[index] == guess[index]
    end
  end
end
module Codebreaker
  class Game
    def initialize(output)
      @output = output
    end

    def start(secret)
      @output.puts "Welcome to Codebreaker!"
      @output.puts "Enter guess:"
      @secret = secret
    end

    def guess(guess)
      @marker = Marker.new(@secret, guess)
      @output.puts "+" * @marker.total_exact_matches +
                   "-" * @marker.total_number_matches
    end
  end
end
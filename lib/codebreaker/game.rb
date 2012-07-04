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
      @output.puts "+" * @marker.exact_match_count +
                   "-" * @marker.number_match_count
    end
  end
end
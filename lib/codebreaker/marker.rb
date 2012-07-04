module Codebreaker
  class Marker
    def initialize(secret, guess)
      @secret = secret
      @guess = guess
    end

    def number_match_count
      total_match_count - exact_match_count
    end

    def total_match_count
      count = 0
      temp_secret_chrs = @secret.chars.to_a
      guess_chrs = @guess.chars.to_a
      guess_chrs.each_index do |i_guess|
        temp_secret_chrs.each_index do |i_secret|
          if temp_secret_chrs[i_secret] == @guess[i_guess]
            temp_secret_chrs.delete_at(i_secret)
            count += 1
            break
          end
        end
      end
      count
    end

    def exact_match_count
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
#!/usr/bin/env ruby
$LOAD_PATH.unshift File.expand_path('../../lib', __FILE__)
require 'codebreaker'

def generate_secret
  choices = %w[ 1 2 3 4 5 6 ]
  (1..4).map { choices.delete_at(rand(choices.length)) }.join
end

game = Codebreaker::Game.new(STDOUT)
secret = generate_secret
at_exit { puts "\n***\nThe secret code was: #{secret}\n***\n"}
game.start(secret)
#game.start("1234")

while (guess = gets.chomp)
  exit -1 unless guess.size > 0
  if game.guess(guess)
    puts "\nCorrect!"
    exit 0
  end
end
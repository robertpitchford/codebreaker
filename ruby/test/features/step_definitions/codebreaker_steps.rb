class Output
  attr_reader :messages
  def initialize
    @messages = []
  end

  def puts(message)
    @messages << message
  end
end

def output
  @output ||= Output.new
end

Given /^I am not playing$/ do
end

When /^I start a new game$/ do
  game = Codebreaker::Game.new(output)
  game.start('1234')
end

Then /^I should see "([^"]*)"$/ do |msg|
  output.messages.should include(msg)
end

Given /^the secret code "([^"]*)"$/ do |secret|
  @game = Codebreaker::Game.new(output)
  @game.start(secret)
end

When /^I guess "([^"]*)"$/ do |guess|
  @game.guess(guess)
end

Then /^the mark should be "([^"]*)"$/ do |mark|
  output.messages.should include(mark)
end
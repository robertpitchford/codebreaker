class Output
  def initialize
    @messages = []
  end

  def message
    @messages
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
  game.start
end

Then /^I should see "([^"]*)"$/ do |msg|
  output.message.should include(msg)
end
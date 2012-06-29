class Greeter
  def greet
    "Hello Cucumber!"
  end
end

Given /^a greeter$/ do
  @greeter = Greeter.new
end

When /^I send it the greet message Then I should see "(.*?)"$/ do |greeting|
  @greeter.greet.should == greeting
end
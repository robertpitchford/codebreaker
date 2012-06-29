require "rubygems"
gem "rspec"

class Greeter
  def greet
    "Hello World!"
  end
end

describe "Hello World!" do

  it "should say Hello World! as a greeting" do

    greeter = Greeter.new
    greeter.greet.should == "Hello World!"
  end
end
class Greeter

end
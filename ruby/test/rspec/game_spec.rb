require_relative 'spec_helper'

module Codebreaker
  describe Game do
    let(:output) { double('output').as_null_object }
    let(:game)   { Game.new(output) }

    describe "#start" do

      it "sends a welcome message" do
        output.should_receive(:puts).with('Welcome to Codebreaker!')
        game.start('1234')
      end

      it "prompts for the first guess" do
        output.should_receive(:puts).with('Enter guess:')
        game.start('1234')
      end
    end

    describe "#guess" do
      context "with 2 number matches and 1 exact match (in that order)" do
        it "sends a mark with '+--'" do
          game.start('1234')
          output.should_receive(:puts).with('+--')
          game.guess('2435')
        end
      end
    end
  end
end

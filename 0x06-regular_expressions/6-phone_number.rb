#!/usr/bin/env ruby
# a ruby script that matches any 10 digit number only. from the given argument
puts ARGV[0].scan(/^[0-9]{10}$/).join
#!/usr/bin/env ruby
# a ruby script that matches hbtn, hbttn, hbt...n from the given argument
puts ARGV[0].scan(/hbt+n/).join
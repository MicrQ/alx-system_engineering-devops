#!/usr/bin/env ruby
# a ruby script that matches hbttn,...,hbtttttn from the given argument.
puts ARGV[0].scan(/hbt{2,5}n/).join
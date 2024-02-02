#!/usr/bin/env ruby
# a ruby script that matches hbtn, hbttn,hbttttn... from the given argument.
puts ARGV[0].scan(/hb(t){2,5}n/).join
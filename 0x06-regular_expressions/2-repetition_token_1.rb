#!/usr/bin/env ruby
# a ruby script that matches htn, hbtn from the given argument using regexp
puts ARGV[0].scan(/hb{0,1}tn/).join
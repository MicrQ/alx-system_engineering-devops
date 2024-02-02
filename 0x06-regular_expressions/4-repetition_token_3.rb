#!/usr/bin/env bash
# a ruby script that maches hbn, hbtn, hbt...n from the given argument
puts ARGV[0].scan(/hbt*n/).join
#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from|to|flag):(\+?\w+|[0-1]:?]+)/).join(',')

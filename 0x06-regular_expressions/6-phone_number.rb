#!/usr/bin/env ruby
phone_number = ARGV[0].gsub(/\D/,'')
if phone_number =~ (^\d{10}$/
    puts phone_number
else
puts "$"
end

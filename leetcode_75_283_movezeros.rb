nums = [0,1,0,3,12]
newnums = []
nums.each do |num|
    unless num == 0
        newnums << num
    end
end

(1..nums.length - newnums.length).each do
    newnums << 0
end

puts newnums.inspect
count = 0
elves = ARGF.slice_when { |line| line.strip.empty? }
calories = elves.map { |elf| elf.map(&:to_i).sum }
puts calories.max

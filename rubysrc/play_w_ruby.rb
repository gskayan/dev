!#/usr/bin/ruby

1.upto(10) {puts "Learn Ruby"}

def checkNum(i)
  begin
    if i.odd? then 
      puts i**2
    elsif i.even? then
      puts Float(i/3)
    end
  end
end

for i in 1...90 do
  checkNum(i)
end
$x=0

until $x > 10 do
  puts $x
  checkNum($x);
  $x +=1;
end

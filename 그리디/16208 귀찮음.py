import sys

n = int(sys.stdin.readline().strip())
iron = list(map(int, sys.stdin.readline().strip().split()))

total = sum(iron)
result = 0
for i in iron: 
  result += i * (total - i)
  total -= i
  
  
print(result)

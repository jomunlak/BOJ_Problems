import sys

n = int(sys.stdin.readline().strip())
i =0
while (i * (i+1)) / 2 <=  n: i += 1
print(i-1)
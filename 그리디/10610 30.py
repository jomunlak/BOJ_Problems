import sys
input = sys.stdin.readline().strip

data = list(input())
n = list(map(int, data))


if 0 in n and sum(n) %3 == 0:
  print(''.join(sorted(data, key = lambda x: -int(x))))
else:
  print(-1)
  

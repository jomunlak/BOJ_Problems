import sys
input = sys.stdin.readline

n = int(input())
x = list(sorted(map(int, input().split())))

i = 0
result = 0
while i < n:
  i += x[i]
  result += 1
print(result)
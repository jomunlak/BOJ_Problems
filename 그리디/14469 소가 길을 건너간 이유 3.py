import sys

n = int(sys.stdin.readline())
cow = [list(map(int, input().split())) for _ in range(n)]
cow.sort(key = lambda x: x[0])

result = 0
for s, e in cow:
  if s > result: result = s
  result += e
print(result)
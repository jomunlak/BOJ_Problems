import sys

n = int(sys.stdin.readline().strip())
firework = list(map(int, sys.stdin.readline().strip().split()))
left = firework[0]
right = firework[-1]
middle = n - 2

result = 0
if middle <= abs(left - right): result = max(left, right) - middle
else:
  middle -= abs(left - right)
  result = min(left, right) - (middle //2) - (1 if middle %2 else 0)
print(result)
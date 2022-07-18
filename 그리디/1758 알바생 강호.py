import sys, heapq

n = int(sys.stdin.readline().strip())
tip = []
for _ in range(n): heapq.heappush(tip, -int(sys.stdin.readline().strip()))

result = 0
for i in range(1, n+1):
  t= -heapq.heappop(tip)
  if t - (i-1) <= 0: break
  else: result += t-(i-1)
print(result)


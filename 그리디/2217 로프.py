import heapq, sys

n = int(sys.stdin.readline())
rope = []
for _ in range(n): heapq.heappush(rope, -int(sys.stdin.readline()))

result = -1
count = 1
for i in range(n):
  r = -heapq.heappop(rope)
  if result < r * count: result = r * count
  count += 1
print(result)
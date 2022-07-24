import sys, heapq
input = sys.stdin.readline
n = int(input())
milk = []
for _ in range(n): heapq.heappush(milk, -int(input()))

result = 0
for i in range(n):
  a = -heapq.heappop(milk)
  if i%3 != 2: result += a
print(result)
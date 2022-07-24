import sys, heapq
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
prev = 0
for i in p:
  result += prev + i
  prev += i
print(result)

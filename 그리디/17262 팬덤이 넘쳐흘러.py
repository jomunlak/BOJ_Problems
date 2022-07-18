import sys, heapq

n = int(sys.stdin.readline().strip())
sList, eList = [], []
for _ in range(n):
  s, e = map(int, sys.stdin.readline().strip().split())
  heapq.heappush(sList, -s)
  heapq.heappush(eList, e)
sMax = -heapq.heappop(sList)
eMin = heapq.heappop(eList)

if eMin >= sMax: print(0)
else: print(sMax - eMin)
  

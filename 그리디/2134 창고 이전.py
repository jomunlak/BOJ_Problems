import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]


stuff = 0 # 옮길 수 있는 물건의 개수 
budget = 0 # 총 비용
aIndex = 0 # a 건물 인덱스
bIndex = 0 # b 건물 인덱스
while aIndex < n and bIndex < m:
  if a[aIndex] < b[bIndex]: # 옮길 공간이 충분할때
    stuff += a[aIndex]
    budget += (aIndex + bIndex + 2) * a[aIndex]
    b[bIndex] -= a[aIndex]
    aIndex += 1
  elif a[aIndex] == b[bIndex]: # 옮길 공간이 딱 맞을때
    stuff += a[aIndex]
    budget += (aIndex + bIndex + 2) * a[aIndex]
    b[bIndex] = 0
    aIndex += 1
    bIndex += 1
  else: # 옮길 공간이 충분하지 않을때
    stuff += b[bIndex]
    budget += (aIndex + bIndex + 2) * b[bIndex]
    a[aIndex] -= b[bIndex]
    bIndex += 1

print(stuff, budget)
  
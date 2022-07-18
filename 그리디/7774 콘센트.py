import sys
input = sys.stdin.readline

n, m = map(int, input().split())

aTob = list(map(int, input().split())) if n != 0 else []
bToa = list(map(int, input().split())) if m != 0 else []
aTob.sort(reverse = True)
bToa.sort(reverse = True)

# b 멀티탭을 꽂을 공간이 없을때마다 a 멀티탭에서 가장 큰 멀티탭을 가져와 하나를 꼽는다?

result = 1
nowA = 1
nowB = 0
i,j = 0, 0
while i < n and j < m:
  if nowB == 0:
    nowA -= 1
    nowB += aTob[i]
    i += 1
  if nowB > 0:
    nowA += sum(bToa[j:min(j+nowB, m)])
    j += nowB
    nowB = 0
  result = max(result, nowA)
print(result)


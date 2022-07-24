import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  data = list(map(int, input().split()))

  data[0] = min(data[0], n - data[0] + 1)
  prev = data[0]
  result = "YES"
  for i in data[1:]:
    if prev > i:
      if prev > n-i+1:
        result = "NO"
        break
      else: prev = n-i+1
    else:
      if prev <= n-i+1 and i > n-i+1: prev = n-i+1
      else: prev= i
  print(result)
# i를 계산중에 i-1까지는 내림차순이 없고, i-1은 (i-1)과 n-(i-1)+1 중 더 작은쪽이라는것이 보장된다    
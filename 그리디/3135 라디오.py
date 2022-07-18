a, b = map(int, input().split())
n = int(input())
fav = [int(input()) for _ in range(n)]

d = abs(a - b) # 두 주파수의 차이

for f in fav: 
  if d > abs(b - f): d = abs(b - f)

if d == abs(a - b): print(d) 
else: print(d + 1) # 즐겨찾기 버튼을 사용했다면 주파수 차이에 1을 더함.

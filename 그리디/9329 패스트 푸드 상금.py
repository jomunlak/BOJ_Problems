import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
  n, m = map(int, sys.stdin.readline().strip().split())
  kInput = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
  k = []
  prize = []
  for tmp in kInput: 
    k.append(tmp[1:-1])
    prize.append(tmp[-1])
  sticker = list(map(int, sys.stdin.readline().strip().split()))

  result = 0
  while True:
    noMore = True
    for i in range(n):
      for j in range(len(k[i])):
        if sticker[k[i][j]-1] == 0:break # 필요한 스티커중 하나라도 0이면 못받음
        if j == len(k[i]) - 1: # 필요한 스티커가 하나씩이라도 있으면 상금을 받음
          noMore = False
          result += prize[i]
          for x in k[i]: sticker[x-1] -= 1 # 사용한 스티커 제거
    if noMore: break
  print(result)



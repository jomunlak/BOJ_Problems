import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  ddang = []
  while True:
    data = int(input())
    if data == 0: break
    else: ddang.append(data)
  
  ddang.sort(reverse = True) # 비싼것부터 사야하지 않을까?
  t = 1
  result = 0
  for d in ddang:
    result += 2 * (d ** t)
    if result > 5*10**6: 
      result = -1
      break
    else: t+= 1
  print(result if result != -1 else "Too expensive")
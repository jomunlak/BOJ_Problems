n = int(input())
hubo = []
for _ in range(n):hubo.append(int(input()))

result = 0
maxNow = -1
try: maxNow = max(hubo[1:])
except: pass

while hubo[0] <= maxNow and n != 1:
  hubo[0] += 1
  hubo[hubo[1:].index(maxNow) + 1]  -= 1 
  maxNow = max(hubo[1:])
  result += 1

print(result)
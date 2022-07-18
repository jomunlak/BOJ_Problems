import sys

J = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
size = ['S', 'M', 'L']


jj = [0]
for _ in range(J):
  data = sys.stdin.readline().strip()
  for i in size:
    if i == data: 
      data = size.index(i) + 1
      break
  jj.append(data)



manjok = [False] * (J+1)
result = 0
for _ in range(N): 
  s, num = sys.stdin.readline().strip().split()
  num = int(num)
  for i in size:
    if s == i: 
      s = size.index(i) + 1
      break
  if manjok[num] == False and  jj[num] >= s:
    manjok[num] = True
    result += 1
print(result)








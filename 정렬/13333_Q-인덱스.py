### 뭔가 어려웠음 


n = int(input())
tmp = list(map(int, input().split()))
ref = [0] *10001
for i in tmp: ref[i] += 1

sum = 0
q = -1
for i in range(10000, -1, -1):
  sum += ref[i]
  if sum >= i: 
    q = i
    break
print(q)
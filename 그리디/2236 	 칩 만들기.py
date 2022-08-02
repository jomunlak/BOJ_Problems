import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bupum = [(i, d) for i, d in enumerate(map(int, input().split()), 1)]
bupum.sort(key = lambda x: x[1], reverse = True)

nresult = [0] * (n+1)
kresult = [] if k <= n else [0] * (k - n)
if k > n: k = n

for i in range(k):
  i, d = bupum[i]
  nresult[i] = i
  kresult.append(i)

for i in kresult + nresult[1:]: print(i)
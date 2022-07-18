n, m , k = map(int, input().split())
p = [0] * (n+1)
data = []
for _ in range(m):
  data = list(map(float, input().split()))
  for i in range(n):
    p[int(data[i*2])] = max(p[int(data[i*2])], data[i*2 + 1])
p.sort(reverse = True)
print(round(sum(p[:k]), 1))
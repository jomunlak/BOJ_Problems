
n, l = map(int, input().split())
pipe = list(map(int, input().split()))


pipe.sort()
result = 1
prev = pipe[0]
for i in range(n):
  if prev + l - 1 < pipe[i]:
    result += 1
    prev = pipe[i]
print(result)
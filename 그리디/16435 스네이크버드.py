n, l = map(int, input().split())
fruit = list(map(int, input().split()))
fruit.sort()

for f in fruit:
  if f <= l: l += 1
print(l)

t = int(input())
for p in range(t):
  n = int(input())
  price = list(map(int, input().split()))
  result = []
  for i in range(n):
    result.append(price[i])
    price.remove(int(price[i] *(4/3)))
  print(f"Case #{p + 1}:", *result)
  
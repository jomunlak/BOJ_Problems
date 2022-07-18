t = int(input())
for _ in range(t):
  j, n = map(int, input().split())
  box = []
  for _ in range(n): 
    a, b = map(int, input().split())
    box.append(a * b)
  box.sort(reverse = True)
  result = 0
  i = 0
  while j >0:
    j -= box[i]
    result += 1
    i += 1
  print(result)
  
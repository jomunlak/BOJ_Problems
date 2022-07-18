n, m = map(int, input().split())
books = []
if n != 0: books = list(map(int, input().split()))


box = m
result = 1
for b in books:
  if b <= box:
    box -= b
  else:
    result += 1
    box = m - b

print(result if n != 0 else 0)
      

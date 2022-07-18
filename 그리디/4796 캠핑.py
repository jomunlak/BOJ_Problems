l, p, v = map(int, input().split())

i = 1
while (l, p, v) != (0,0,0):
  x = divmod(v, p)
  result = x[0] * l + min(x[1], l)
  print(f"Case {i}:",result)
  i +=1 
  l, p, v = map(int, input().split())

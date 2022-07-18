

while True:
  n = int(input())
  if n == 0: break

  stop = [int(input()) for _ in range(n)]
  stop.sort()
  prev = 0
  for s in stop:
    if s - prev > 200: 
      print("IMPOSSIBLE")
      break
    if 1422 - s <= 100:
      print("POSSIBLE")
      break
    if s == stop[-1]: print("IMPOSSIBLE")
    prev = s
    
while True:
  x, y, w = input().split()
  x, y = int(x), int(y)
  w = float(w)
  if x == 0 and y ==0 and w ==0.0: break
  xi = list(map(float, input().split()))
  yi = list(map(float, input().split()))
  
  
  isXPerfect = False
  xi.sort()
  if xi[0] - w/2 > 0  or xi[-1] + w/2 < 75:
    pass
  else:
    for i in range(1, x-1):
      if w < xi[i+1] - xi[i]: break
      if i == x-2: isXPerfect = True



  isYPerfect = False
  yi.sort()
  if yi[0] - w/2 > 0  or yi[-1] + w/2 < 100:
    pass
  else:
    for i in range(1, y-1):
      if yi[i] + w/2 < yi[i+1] - w/2: break
      if i == y-2: isYPerfect = True

  if isXPerfect and isYPerfect: print("YES")
  else: print("NO")
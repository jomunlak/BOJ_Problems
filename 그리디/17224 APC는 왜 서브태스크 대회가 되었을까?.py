n, l, k = map(int, input().split())
probs = []
for _ in range(n):
  probs.append(tuple(map(int, input().split())))

rate = 0
for _ in range(k):
  hsolve, lsolve = False, False
  for i in range(len(probs)):
    if probs[i][1] <= l:
      hsolve = True
      rate += 140
      del probs[i]
      break
  if not hsolve:
    for i in range(len(probs)):
      if probs[i][0] <= l:
        lsolve = True
        rate += 100
        del probs[i]
        break
  if not hsolve and not lsolve: break
  
print(rate)

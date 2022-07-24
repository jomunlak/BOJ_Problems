import sys

T = int(sys.stdin.readline())
for _ in range(T):
  n = int(sys.stdin.readline())
  card = list(sys.stdin.readline().split())

  f = []
  r = []
  first = card[0]
  for c in card[1:]:
    if first >= c: 
      f.append(c)
      first = c
    else: 
      r.append(c)
  f.reverse()
  print(''.join(f) + card[0] + ''.join(r))



  



T = int(input())
for _ in range(T):
  n = int(input())
  old = list(input().split())
  new = list(input().split())
  old.sort()
  new.sort()
  if old == new: print("NOT CHEATER")
  else: print("CHEATER")
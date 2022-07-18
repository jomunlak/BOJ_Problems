n, s, r = map(int, input().split())
broken =list(map(int, input().split()))
spair =list(map(int, input().split()))
spair.sort()

for s in spair:
  if s in broken: broken.remove(s)
  elif s-1 in broken: broken.remove(s-1)
  elif s+1 in broken: broken.remove(s+1)

print(len(broken))
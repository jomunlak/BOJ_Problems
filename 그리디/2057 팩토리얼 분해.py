def factorial(n):
  if n <= 1 : return 1
  else: return n *factorial(n-1)

n = int(input())
facto = [factorial(i) for i in range(21, -1, -1)]

nn = n
for f in facto:
  if n >= f: n -= f

if nn != 0 and n == 0: print("YES")
else: print("NO")

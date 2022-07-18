import sys
n, m= map(int, sys.stdin.readline().strip().split())
sett, indiv = 1000, 1000
for _ in range(m): 
  a, b = map(int, sys.stdin.readline().strip().split())
  sett = min(sett, a); indiv = min(indiv, b)

result = min([sett * (n//6) + indiv * (n%6), indiv * n, sett * (n//6 + (1 if n%6 else 0))])

print(result)



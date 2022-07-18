import sys
n= int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
a.sort(); b.sort(reverse =True)
result = 0
for i in range(n): result += a[i] * b[i]
print(result)

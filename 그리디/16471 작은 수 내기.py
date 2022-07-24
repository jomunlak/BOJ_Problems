# import sys
# input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()



result = 0
for i in range(n//2 + 1):
  if a[i] < b[i + n//2]:
    result+= 1

print("YES" if (n + 1)/2 <= result else "NO")
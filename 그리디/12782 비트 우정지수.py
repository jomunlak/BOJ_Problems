import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  str1, str2 = input().split()
  count1 = 0
  count0 = 0
  for a, b in zip(str1, str2):
    if a!= b:
      if a == '1': count1 += 1
      else: count0 += 1
  print(max(count1, count0))
  
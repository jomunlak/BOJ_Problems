import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  if n == 1: n = 2 # n==1일경우 0으로 출력되는 문제를 해결
  div = [0] * 10
  
  for i in range(9, 1, -1):
    while n%i ==0:
      n = n//i
      div[i] += 1
      
  result = sum(div) if n == 1 else -1
  print(result)
  

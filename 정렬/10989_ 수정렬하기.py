import sys
N = int(sys.stdin.readline().strip())
myList = [0] * 10001
for _ in range(N): myList[int(sys.stdin.readline().strip())] += 1
for i in range(1, 10001):
  if myList[i] != 0:
    for j in range(myList[i]) : print(i)

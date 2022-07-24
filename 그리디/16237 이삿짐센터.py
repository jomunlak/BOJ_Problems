# import sys
# input = sys.stdin.readline

stuff = list(map(int, input().split()))

result = 0
box = 0
while sum(stuff) != 0:
  if box == 0:
    box = 5
    result += 1

  
  if stuff[4] > 0 and box == 5:
    box -= 5
    stuff[4] -= 1
  elif stuff[3] > 0 and box >= 4:
    box -= 4
    stuff[3] -= 1
  elif stuff[2] > 0 and box >= 3:
    box -= 3
    stuff[2] -= 1
  elif stuff[1] > 0 and box >= 2:
    box -= 2
    stuff[1] -= 1
  elif stuff[0] > 0 and box >= 1:
    box -= 1
    stuff[0] -= 1
  else:
    box = 0

print(result)
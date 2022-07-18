n, a, b = map(int, input().split())
subject = [list(map(int, input().split())) for _ in range(10)]


result = "Nae ga wae"
for i in range(8 - n):
  a += subject[i][0] * 3
  b += subject[i][0] * 3 + min(6 - subject[i][0], subject[i][1]) * 3
  if a >= 66 and b >= 130: result = "Nice"
  
print(result )
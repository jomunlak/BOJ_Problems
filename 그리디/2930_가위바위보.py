
def dual (sm, fList): # sm을 fList와 비교하여 한 라운드 점수를 구하는 함수
  rateSum = 0
  for f in fList:
    if sm == f:rateSum += 1
    elif (sm =='P' and f =='S') or (sm == 'R' and f == 'P') or (sm == 'S' and f == 'R'): rateSum += 0
    else:rateSum += 2
  return rateSum

R = int(input())
sm = input()
N = int(input())
friend = []
for _ in range(N): friend.append(input())
friend = list(zip(*friend))
RSP = ['R', 'S', 'P']


rating = 0
maxRating = 0

for i in range(R): rating += dual(sm[i], friend[i])
for i in range(R):
  maxTmp = 0
  for j in range(3): 
    if maxTmp < dual(RSP[j], friend[i]): maxTmp = dual(RSP[j], friend[i])
  maxRating += maxTmp
  
print(rating)
print(maxRating)

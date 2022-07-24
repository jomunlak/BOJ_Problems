import sys
input = sys.stdin.readline

def even_odd(x): # 짝수면 True, 홀수면 False
  if int(x)%2 == 0: return True
  else: return False

n = int(input())
data = list(map(even_odd, input().split()))

total = n * (n-1)//2 # 리스트 모든 원소의 인덱스 합
count = 0 # 짝수의 개수
indexSum = 0 # 짝수의 인덱스 합

for i, x in enumerate(data):
  if x: 
    count += 1
    indexSum += i

# 한 원소를 다른 원소의 위치로 보내기위해 필요한 교환 시행횟수는 두 원소의 인덱스의 차와 같다

left = indexSum - count * (count-1)//2 # 짝수를 왼쪽 정렬했을때의 시행횟수
right = total - ((n - count) *(n-count-1)//2) - indexSum # 짝수를 오른쪽 정렬했을때의 시행횟수




print(min(left, right))
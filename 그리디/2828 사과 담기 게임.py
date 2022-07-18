n, m = map(int, input().split()) # n = 스크린 크기, m = 바구니 크기
j= int(input())
apple = [int(input()) for _ in range(j)]



result = 0 # 이동해야할 거리의 합
left = 1
right = m #각각 바구니의 왼쪽, 오른쪽 좌표
for a in apple:
  if a in range(left, right + 1): continue
  else: 
    if a < left:
      result += left - a
      left = a
      right = left + m -1
    else:
      result += a - right
      right = a
      left = right - m + 1

print(result)
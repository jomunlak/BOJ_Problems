n = int(input())
coin1 = list(map(int, input().split()))
coin2 = list(map(int, input().split()))
result = 0
for c in coin1: result += abs(c)
for c in coin2: result += abs(c)
print(result)
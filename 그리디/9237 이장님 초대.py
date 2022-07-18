n = int(input())
tree = [*map(int, input().split())]


# 가장 오래걸리는 묘목부터 하나씩 골라서      
tree.sort(reverse = True)


a = -1
result = 0
for i in range(n):
  if a < tree[i]: a= tree[i]
  a -= 1
  if i == n-1:
    result = (i + 3) + a
print(result)
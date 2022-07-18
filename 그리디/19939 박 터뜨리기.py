n , k = map(int, input().split())

result = 0
if n < (k *(k+1)) //2: result = -1
else: 
  n -= (k *(k+1)) //2
  result = k if n%k != 0 else k-1
print(result)

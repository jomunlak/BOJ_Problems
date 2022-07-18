n = int(input())

result = 0
if n%5 == 0: result = n//5
elif n%5 == 1: result = (n//5 + 1 if n//5>=1 else -1)
elif n%5 == 2: result = (n//5 + 2 if n//5>=2 else -1)
elif n%5 == 3: result = n//5 + 1
elif n%5 == 4: result = (n//5 + 2 if n//5>=1 else -1)

print(result)
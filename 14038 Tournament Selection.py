count = 0
for _ in range(6): 
    if input() == 'W': count += 1
if count >= 5 : result = 1
elif count >= 3 : result = 2
elif count >= 1 : result = 3
else : result = -1

print(result)

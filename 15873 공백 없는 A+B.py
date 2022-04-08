
x = input()
result = 0
if len(x) <=2 : result = int(x[0]) + int(x[1])
elif len(x) == 3:
    if x[1] == '0':
        result = 10 + int(x[2])
    elif x[2] == '0':
        result = 10 + int(x[0])
elif len(x) == 4 : result = 20

print(result)

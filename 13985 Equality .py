quiz = input()
answer = eval(quiz[:5])
result = "YES" if answer == int(quiz[8]) else "NO"

print(result)

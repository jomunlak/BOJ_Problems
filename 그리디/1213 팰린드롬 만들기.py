# 회문 만들기
data = input()
alpha = [0] * 26
for i in data: alpha[ord(i) - 65] += 1

n = len(data)
result = []
middle = ''
for i in range(26):
  if alpha[i] %2 == 0: result.append(chr(i + 65) * (alpha[i] //2))
  else:
    if n%2== 1 and middle == '': 
      result.append(chr(i + 65) * (alpha[i] //2))
      middle = chr(i + 65)
    else:
      n = -1
      break
if n == -1: print("I'm Sorry Hansoo")
else: print(''.join(result) + middle + ''.join(result[::-1]))
      


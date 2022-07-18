string = input().split('.')

impossible = False
result = []
for i in range(len(string)):
  if len(string[i])%2 != 0:
    impossible = True
    break
  result.append("AAAA" * (len(string[i]) // 4) + "BB" * ((len(string[i])%4)//2))


if impossible: print(-1)
else: print(".".join(result))
    
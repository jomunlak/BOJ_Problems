
while True:
  try:
    T, S = input().split()
    i, j = 0, 0
    result = "No"
    while True:
      if i >= len(S) or j >= len(T): 
        break
      if S[i] == T[j]:
        if j == len(T) - 1: 
          result = "Yes"
          break
        i += 1
        j += 1
      else:i += 1
    print(result)

  except:
    break

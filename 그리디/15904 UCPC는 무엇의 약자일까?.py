
string = input()
UCPC = "UCPC"

i, j = 0, 0
while i< 4 and j < len(string):
  if UCPC[i] == string[j]:
    i += 1
    j += 1
  else:
    j += 1

if i == 4: print("I love UCPC")
else: print("I hate UCPC")
T = int(input())
for _ in range(T):
  strA, strB  = input().split()
  isAnagram = True
  if len(strA) != len(strB): isAnagram = False
  else:
    for a, b in zip(sorted(strA), sorted(strB)):
      if a != b: 
        isAnagram = False
        break

  if isAnagram: print(strA,"&",strB,"are anagrams.")
  else: print(strA,'&',strB,"are NOT anagrams.")
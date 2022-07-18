import sys
case = 1
while True:
  org = sys.stdin.readline().strip()
  rtv = sys.stdin.readline().strip()
  if org == "END" and rtv == "END": break
  
  isSame = True
  if len(org) != len(rtv): isSame = False
  else: 
    for o, r in zip(sorted(org), sorted(rtv)): 
      if o != r: 
        isSame = False
        break
  if isSame: print(f"Case {case}: same")
  else: print(f"Case {case}: different")
  case += 1
      
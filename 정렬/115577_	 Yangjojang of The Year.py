T = int(input())
for _ in range(T):
  N = int(input())
  name = ""
  soju = 0
  for _ in range(N):
    input_name, input_soju = input().split()
    input_soju = int(input_soju)
    if input_soju > soju: 
      name = input_name
      soju = input_soju
  print(name)
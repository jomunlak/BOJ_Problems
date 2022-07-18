import sys

obj = sys.stdin.readline().strip()
source = sys.stdin.readline().strip()

count = 0
n = 0
while n + len(source) <= len(obj):
  if obj[n:n+len(source)] == source:
    count+=1
    n += len(source)
  else:
    n += 1


print(count)



# while True:
#   print(obj)
#   if obj.find(source) == -1: break
#   else:
#     obj = obj.replace(source, '', 1)
#     count += 1

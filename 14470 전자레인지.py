
meat =  int(input())
goal = int(input())
frozen = int(input())
haedong = int(input())
cook = int(input())

result = 0

if meat < 0 : 
    result += abs(meat) * frozen
    result += haedong
    meat = 0
if meat < goal:
    result += (goal - meat) * cook
print(result)

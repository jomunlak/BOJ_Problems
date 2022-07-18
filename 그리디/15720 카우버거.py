a, b, c = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse = True)
side.sort(reverse = True)
drink.sort(reverse = True)

l = min(len(burger), len(side), len(drink))

result1 = sum(burger + side +drink)
result2 = int(sum(burger[:l] + side[:l] + drink[:l]) *0.9 + sum(burger[l:] + side[l:] + drink[l:]))

print(result1)
print(result2)









number = int(input())

hundres = ((number // 100)%100)
tens = ((number // 10)% 10)
ones = (number % 10)

print(hundres+tens+ones)
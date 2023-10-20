a = int(input())
b = a % 10
c = (a % 100) // 10
d = a // 100
print(d * 100 + b + c * 10)
print(d * 100 + c + b * 10)
print(c * 100 + b + d * 10)
print(c * 100 + d + b * 10)
print(b * 100 + c + d * 10)
print(b * 100 + d + c * 10)
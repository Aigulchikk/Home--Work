a = int(input())
b = (a % 10) 
c = (a % 100) // 10
d = a // 100
print("Сумма цифр =", b + c + d)
print("Произведение цифр =", b * c * d)
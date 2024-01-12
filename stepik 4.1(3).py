i = int(input())
if ( (i // 1000 % 10) + (i % 10)) == ((i // 100 % 10) - (i % 100 // 10)):
    print("ДА")
else:
    print("НЕТ")
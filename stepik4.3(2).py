a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
if (a == b or a == c or b == c) and (a != c or a != b or b != c):
    print("Равнобедренный")
if a != b and a != c and c != b:
    print("Разносторонний")
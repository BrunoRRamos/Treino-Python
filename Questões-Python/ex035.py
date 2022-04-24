a = float(input())
b = float(input())
c = float(input())

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print(True)

else:
    print(False)
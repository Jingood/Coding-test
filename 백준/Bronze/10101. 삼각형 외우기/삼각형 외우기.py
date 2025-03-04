a = int(input())
b = int(input())
c = int(input())

total = a + b + c
if total == 180:
    
    if a == b and a == c:
        print("Equilateral")
    
    elif (a == b and b != c) or (a != b and b == c) or (a == c and b != c):
        print("Isosceles")
    
    else:
        print("Scalene")

else:
    print("Error")
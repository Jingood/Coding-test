while 1 :
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    else:
        total = a + b + c
        if total - max(a, b, c) <= max(a, b, c):
            print("Invalid")

        else:
            if a == b and a == c:
                print("Equilateral")

            elif (a == b and b != c) or (a == c and b != c) or (b == c and a != c):
                print("Isosceles")
            
            else:
                print("Scalene")
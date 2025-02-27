t = 1
while t > 0:
    n = int(input())
    factos = []

    if n == -1:
        break
    
    for i in range(1, n):
        if n % i == 0:
            factos.append(i)
    
    if sum(factos) == n:
        print(n, " = ", " + ".join(str(i) for i in factos), sep="")
    
    else:
        print(f"{n} is NOT perfect.")

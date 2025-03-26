import sys 

N = int(sys.stdin.readline())

crd = list(map(int, sys.stdin.readline().split()))

temp = sorted(list(set(crd)))
dic = {temp[i] : i for i in range(len(temp))}

for i in crd:
    print(dic[i], end=" ")

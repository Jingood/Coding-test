import sys

input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]
dic = dict()

arr.sort()
print(round(sum(arr)/N))
print(arr[N//2])

for num in arr:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

mx = max(dic.values())
mx_dic = []

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

print(max(arr) - min(arr))
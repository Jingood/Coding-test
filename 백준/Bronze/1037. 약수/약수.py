N = int(input())
gcp = list(map(int, input().split()))

answer = min(gcp) * max(gcp)

print(answer)
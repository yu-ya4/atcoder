N = int(input())
A =list(map(int, input().split()))

cnt = 0
for i in A:
    if i < 0: cnt += 1

A_abs = list(map(abs, A))
minmum = min(A_abs)

if cnt % 2 == 0:
    ans = sum(A_abs)
else:
    ans = sum(A_abs) - 2*minmum

print(ans)

import functools
import copy

N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

l = [0] * N  #L_i, i = 0, 1, 2, ..., N-1
for i in range(N):
    if i == 0:
        continue
    else:
        l[i] = gcd(l[i-1], A[i-1])

r = [0] * N #R_i, i = 0, 1, 2, ..., N-1
for j in range(N):
    if j == 0:
        continue
    else:
        r[N-j-1] = gcd(r[N-j], A[N-j])

m = [0] * N
for i in range(N):
    m[i] = gcd(l[i], r[i])

print(max(m))

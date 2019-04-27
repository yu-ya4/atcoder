import functools
import copy

N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n = 0

if N == 2:
    n = max(A)
else:
    for i in range(N):
        l = copy.copy(A)
        l.pop(i)
        res = functools.reduce(lambda x, y: gcd(x, y), l)
        if res > n:
            n = res
print(n)

n, k = list(map(int, input().split()))
ds = list(map(str, input().split()))

while(1):
    n_str = list(str(n))
    if sum([i in ds for i in n_str]) == 0:
        print(n)
        break
    n += 1

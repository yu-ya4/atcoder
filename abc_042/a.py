a = list(map(int, input().split()))
if sum(a) == 17 and a.count(5) == 2:
    print("YES")
else:
    print("NO")

n = 15
p = 3
i = 0
l = 1
r = n
while l < r and i<=n:
    if i%2 == 0:
        l += p
    else:
        r -= p
    i += 1
if n%p == 0:
    print(r)
else:
    print(r+1)
        
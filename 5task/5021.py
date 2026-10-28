ans = []

for N in range(1, 10_000):
    R = f'{N:o}'
    R = ''
    n = N
    while n > 0:
        R = str(n % 3) + R
        n //= 3
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R = R + f'{(N % 3) * 4:01b}'

        x = (N % 3) * 4
        extra = ''
        while x > 0:
            extra = str(x % 3) + extra
            x //= 3
        R = R[:-len(f'{(N % 3) * 4:01b}')] + extra

    R = int(R, 3)

    if R < 199:
        ans.append(N)

print(max(ans))


def ds_multof_pfs(nMin, nMax):
    def prime_factors_sum(n):
        total = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                total += d
                n //= d
            d += 1
        if n > 1:
            total += n
        return total

    def divisors_sum(n):
        total = 0
        d = 1
        while d * d <= n:
            if n % d == 0:
                total += d
                if d != n // d:
                    total += n // d
            d += 1
        return total

    result = []
    for n in range(nMin, nMax + 1):
        pfs = prime_factors_sum(n)
        if pfs == 0:
            continue
        ds = divisors_sum(n)
        if ds % pfs == 0:
            result.append(n)

    return result


print(ds_multof_pfs(10, 100))
print(ds_multof_pfs(20, 120))
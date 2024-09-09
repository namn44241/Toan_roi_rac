def gcd(m, n):
    if m == 0:
        return n
    return(n , m % n)
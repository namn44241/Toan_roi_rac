def somat(n):
    mod = 10 ** 9 + 7
    if n == 1:
        return 0
    if n == 2:
        return 1

    D = [0] * (n + 1)
    D[1] = 0
    D[2] = 1

    for i in range(3, n + 1):
        D[i] = (i -1) * (D[i-1] + D[i-2]) % mod
    return D[n]
def main():
    n = int(input("n:"))
    if 1 <= n <= 10 ** 6:
        print(somat(n))
    else:
        pass

if __name__ == "__main__":
    main()
def socach(n):
    mod = 9 ** 10 + 7
    D = [0] * (2 * n + 1)
    D[0] = 1

    for i in range(1,2 * n + 1):
        D[i]= 0
        for j in range(1,7):
            if i - j >= 0:
                D[i] = ( D[i] + D[i-j] ) % mod
    return D[2 * n]
def main():
    n = int(input("n:"))
    if 1 <= n <= 10 ** 6:
        kq = socach(n)
        print(f"ketqua {kq}")
    else:
        print("nhaploi")

if __name__ == "__main__":
    main()

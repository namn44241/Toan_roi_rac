# Cho 2 số nguyên dương M, N (M, N < 10^6),
# sử dụng đệ quy tính ước chung lớn nhất của M và N.

def gcd(M, N):
    if N == 0:
        return M
    return gcd(N, M % N)


def main():
    M = int(input("Nhập M: "))
    N = int(input("Nhập N: "))

    if 0 < M < 10 ** 6 and 0 < N < 10 ** 6:
        result = gcd(M, N)
        print(f"Ước chung lớn nhất của {M} và {N} là: {result}")
    else:
        print("Giá trị của M và N không hợp lệ.")


if __name__ == "__main__":
    main()

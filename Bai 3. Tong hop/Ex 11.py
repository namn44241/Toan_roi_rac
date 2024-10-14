# Cho số N ( 1 < N < 10^6),
# sử dụng đệ quy tính số chữ số và tổng các chữ số của N.

def dem(N):
    if N == 0:
        return 0
    return 1 + dem(N // 10)


def tong(N):
    if N == 0:
        return 0
    return (N % 10) + tong(N // 10)


def main():
    N = int(input("Nhập số N (1 < N < 10^6): "))

    if 1 < N < 10 ** 6:
        a = dem(N)
        b = tong(N)

        print(f"Số chữ số của {N} là: {a}")
        print(f"Tổng các chữ số của {N} là: {b}")
    else:
        print("Giá trị của N không hợp lệ.")


if __name__ == "__main__":
    main()

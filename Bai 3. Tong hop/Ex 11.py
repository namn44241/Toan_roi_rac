# Cho số N ( 1 < N < 10^6),
# sử dụng đệ quy tính số chữ số và tổng các chữ số của N.

def count_digits(N):
    if N == 0:
        return 0
    return 1 + count_digits(N // 10)


def sum_digits(N):
    if N == 0:
        return 0
    return (N % 10) + sum_digits(N // 10)


def main():
    N = int(input("Nhập số N (1 < N < 10^6): "))

    if 1 < N < 10 ** 6:
        digit_count = count_digits(N)
        digit_sum = sum_digits(N)

        print(f"Số chữ số của {N} là: {digit_count}")
        print(f"Tổng các chữ số của {N} là: {digit_sum}")
    else:
        print("Giá trị của N không hợp lệ.")


if __name__ == "__main__":
    main()

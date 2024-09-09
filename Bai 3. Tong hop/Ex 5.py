# Cho số tự nhiên n (1 <= n <= 10^6).
# Hãy tính số mất thứ tự D(n),
# kết quả lấy dư của phép chia cho 10^9+7

def derangement(n):
    MOD = 10 ** 9 + 7

    if n == 1:
        return 0
    elif n == 2:
        return 1

    D = [0] * (n + 1)
    D[1] = 0
    D[2] = 1

    for i in range(3, n + 1):
        D[i] = (i - 1) * (D[i - 1] + D[i - 2]) % MOD
    return D[n]


def main():
    n = int(input("Nhập n: "))

    if 1 <= n <= 10 ** 6:
        result = derangement(n)
        print(f"Số mất thứ tự D({n}) là: {result}")
    else:
        print("Giá trị của n không hợp lệ.")


if __name__ == "__main__":
    main()
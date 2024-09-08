# Cho 2 số tự nhiên n và k (0 <= k <= n <= 100).
# Hãy tính số cấu hình tổ hợp chập k của n,
# kết quả lấy phần dư của phép chia cho 10^9+7

def giaithua(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result


def pheptinh(n, k, mod):
    if k == 0 or k == n:
        return 1
    tinhtuso = giaithua(n, mod)
    tinhmauso = (giaithua(k, mod) * giaithua(n - k, mod)) % mod
    return (tinhtuso / tinhmauso) % mod


def main():
    MOD = 10 ** 9 + 7
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))

    if 0 <= k <= n <= 100:
        result = pheptinh(n, k, MOD)
        print(f"Số cấu hình tổ hợp chập {k} của {n} là: {result}")
    else:
        print("Giá trị của n hoặc k không hợp lệ.")


if __name__ == "__main__":
    main()

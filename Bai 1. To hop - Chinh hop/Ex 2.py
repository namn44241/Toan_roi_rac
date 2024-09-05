# Cho 2 số tự nhiên n và k (0 <= k <= n <= 100).
# Hãy tính số cấu hình tổ hợp chập k của n,
# kết quả lấy phần dư của phép chia cho 10^9+7

def factorial_mod(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result


def combination(n, k, mod):
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    numerator = factorial_mod(n, mod)
    denominator = (factorial_mod(k, mod) * factorial_mod(n - k, mod)) % mod
    # Sử dụng lũy thừa nghịch đảo để tính kết quả cuối cùng
    denominator_inverse = pow(denominator, mod - 2, mod)
    return (numerator * denominator_inverse) % mod


def main():
    MOD = 10 ** 9 + 7
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))

    if 0 <= k <= n <= 100:
        result = combination(n, k, MOD)
        print(f"Số cấu hình tổ hợp chập {k} của {n} là: {result}")
    else:
        print("Giá trị của n hoặc k không hợp lệ.")


if __name__ == "__main__":
    main()

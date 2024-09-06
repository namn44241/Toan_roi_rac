# Cho 2 số tự nhiên n và k (0 <= k <= n <= 10^9).
# Hãy tính số cấu hình chỉnh hợp lặp chập k của n,
# kết quả lấy phần dư của phép chia cho 10^9+7

def power_mod(a, b, mod):
    result = 1
    base = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        b //= 2
    return result

def main():
    MOD = 10 ** 9 + 7
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))

    if 0 <= k <= n <= 10 ** 9:
        result = power_mod(n, k, MOD)
        print(f"Số cấu hình chỉnh hợp lặp chập {k} của {n} là: {result}")
    else:
        print("Giá trị của n hoặc k không hợp lệ.")

if __name__ == "__main__":
    main()

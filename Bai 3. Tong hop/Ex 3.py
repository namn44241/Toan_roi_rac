# Cho 2 số tự nhiên n và k
# (0 <= k <= n <= 10^9).
# Hãy tính số cấu hình chỉnh hợp lặp chập k của n,
# kết quả lấy phần dư của phép chia cho 10^9+7

def chinh_hop_lap(n, k):
    MOD = 10**9 + 7
    kq = 1
    for i in range(k):
        kq = (kq * n) % MOD
    return kq

def main():
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))

    if 0 <= k <= n <= 10 ** 9:
        result = chinh_hop_lap(n, k)
        print(f"Số cấu hình chỉnh hợp lặp chập {k} của {n} là: {result}")
    else:
        print("Giá trị của n hoặc k không hợp lệ.")

if __name__ == "__main__":
    main()
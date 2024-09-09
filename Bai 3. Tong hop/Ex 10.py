# Cho 2 số n, k ( 2 <= k <= n <= 10^3).
# Sử dụng đệ quy tính số tổ hợp chập k của n.

def combination(n, k):
    if k == 0 or k == n:
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k)


def main():
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))

    if 2 <= k <= n <= 1000:
        result = combination(n, k)
        print(f"Số tổ hợp chập {k} của {n} là: {result}")
    else:
        print("Giá trị của n và k không hợp lệ.")


if __name__ == "__main__":
    main()

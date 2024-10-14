# Nhập 1 số nguyên dương n chia hết cho 6 (n < 1000),
# liệt kê các số Fibonaci thứ 1, n/3, n/2 và n.

def fibonacci(k):
    if k == 1:
        return 0
    elif k == 2:
        return 1

    a, b = 0, 1
    for i in range(3, k + 1):
        a, b = b, a + b
    return b


def main():
    n = int(input("Nhập số nguyên dương n chia hết cho 6 (n < 1000): "))

    if n % 6 == 0 and 0 < n < 1000:
        a = fibonacci(1)
        b = fibonacci(n // 3)
        c = fibonacci(n // 2)
        d = fibonacci(n)

        print(f"Số Fibonacci thứ 1: {a}")
        print(f"Số Fibonacci thứ {n // 3}: {b}")
        print(f"Số Fibonacci thứ {n // 2}: {c}")
        print(f"Số Fibonacci thứ {n}: {d}")
    else:
        print("Giá trị của n không hợp lệ. n phải chia hết cho 6 và nhỏ hơn 1000.")


if __name__ == "__main__":
    main()

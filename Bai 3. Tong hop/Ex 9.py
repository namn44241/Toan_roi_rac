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
        fib_1 = fibonacci(1)
        fib_n3 = fibonacci(n // 3)
        fib_n2 = fibonacci(n // 2)
        fib_n = fibonacci(n)

        print(f"Số Fibonacci thứ 1: {fib_1}")
        print(f"Số Fibonacci thứ {n // 3}: {fib_n3}")
        print(f"Số Fibonacci thứ {n // 2}: {fib_n2}")
        print(f"Số Fibonacci thứ {n}: {fib_n}")
    else:
        print("Giá trị của n không hợp lệ. n phải chia hết cho 6 và nhỏ hơn 1000.")


if __name__ == "__main__":
    main()

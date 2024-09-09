# Cho số tự nhiên n (1 <= n <= 10^12),
# số tự nhiên k (1<=k<=10),
# k số nguyên tố khác nhau.
# Hãy đếm số các số tự nhiên nhỏ hơn hoặc bằng n và không chia hết cho bất cứ số nguyên tố nào trong k số.


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def count_non_divisible(n, primes):
    def count_divisible(mask):
        product = 1
        for i in range(len(primes)):
            if mask & (1 << i):
                product = lcm(product, primes[i])
        return n // product

    total = 0
    for mask in range(1, 1 << len(primes)):
        if bin(mask).count('1') % 2 == 1:
            total += count_divisible(mask)
        else:
            total -= count_divisible(mask)

    return n - total


def main():
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))
    primes = list(map(int, input("Nhập k số nguyên tố khác nhau: ").split()))

    if 1 <= n <= 10 ** 12 and 1 <= k <= 10 and len(primes) == k:
        result = count_non_divisible(n, primes)
        print(
            f"Số các số nhỏ hơn hoặc bằng {n} và không chia hết cho bất kỳ số nguyên tố nào trong {k} số đã cho là: {result}")
    else:
        print("Giá trị đầu vào không hợp lệ.")


if __name__ == "__main__":
    main()
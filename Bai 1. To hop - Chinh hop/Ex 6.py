# Cho số tự nhiên n (1 <= n <= 10^12),
# số tự nhiên k (1<=k<=10),
# k số nguyên tố khác nhau.
# Hãy đếm số các số tự nhiên nhỏ hơn hoặc bằng n và không chia hết cho bất cứ số nguyên tố nào trong k số.

import math
from itertools import combinations

MOD = 10 ** 9 + 7


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def count_non_divisible(n, primes):
    count = 0
    k = len(primes)

    for r in range(1, k + 1):
        for subset in combinations(primes, r):
            lcm_value = 1
            for prime in subset:
                lcm_value = lcm(lcm_value, prime)
                if lcm_value > n:
                    break
            if lcm_value > n:
                continue
            if r % 2 == 1:
                count += n // lcm_value
            else:
                count -= n // lcm_value

    return n - count


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

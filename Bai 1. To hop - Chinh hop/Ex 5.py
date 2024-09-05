# Cho số tự nhiên n, m (1 <= n, m <= 100),
# dãy Y1, Y2, ..., Yn (Y1 + Y2 + ... + Yn <= n) .
# Hãy đếm số nghiệm của phương trình X1+X2+...+Xn =m sao cho Xi >= Yi.
# Kết quả lấy dư của phép chia cho 10^9+7

MOD = 10 ** 9 + 7


def factorial_mod(n, mod):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    return fact


def inverse_factorial_mod(fact, mod):
    inv_fact = [1] * len(fact)
    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in range(len(fact) - 2, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return inv_fact


def combination(a, b, fact, inv_fact, mod):
    if b > a or b < 0:
        return 0
    return fact[a] * inv_fact[b] % mod * inv_fact[a - b] % mod


def count_solutions(n, m, Y):
    sum_Y = sum(Y)
    m_prime = m - sum_Y
    if m_prime < 0:
        return 0

    fact = factorial_mod(m_prime + n, MOD)
    inv_fact = inverse_factorial_mod(fact, MOD)

    return combination(m_prime + n - 1, n - 1, fact, inv_fact, MOD)


def main():
    n = int(input("Nhập n: "))
    m = int(input("Nhập m: "))
    Y = list(map(int, input("Nhập dãy Y (cách nhau bởi dấu cách): ").split()))

    if 1 <= n <= 100 and 1 <= m <= 100 and len(Y) == n and sum(Y) <= n:
        result = count_solutions(n, m, Y)
        print(f"Số nghiệm của phương trình là: {result}")
    else:
        print("Giá trị đầu vào không hợp lệ.")


if __name__ == "__main__":
    main()

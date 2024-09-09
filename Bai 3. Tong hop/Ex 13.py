# Cho 1 số nguyên dương N,
# giải bài toán tháp Hà Nội với N.

def hanoi(n, a, b, c):
    if n == 1:
        print(f"Di chuyển đĩa 1 từ {a} sang {b}")
        return
    hanoi(n - 1, a, c, b)
    # Di chuyển đĩa lớn nhất từ cột nguồn sang cột đích
    print(f"Di chuyển đĩa {n} từ {a} sang {b}")
    # Di chuyển n-1 đĩa từ cột phụ sang cột đích
    hanoi(n - 1, c, b, a)


def main():
    N = int(input("Nhập số đĩa N: "))

    if N > 0:
        print(f"Giải bài toán Tháp Hà Nội với {N} đĩa:")
        hanoi(N, 'A', 'C', 'B')
    else:
        print("Số đĩa phải là số nguyên dương.")


if __name__ == "__main__":
    main()

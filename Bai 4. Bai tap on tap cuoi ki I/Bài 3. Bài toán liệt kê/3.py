# Nhập vào 1 số tự nhiên n < 1000. Liệt kê tất cả các tập con của tập {1, 2, ..., n}.

def chuoi(n):
    def quilui(start, current):
        result.append(current[:])
        for i in range(start, n + 1):
            current.append(i)
            quilui(i + 1, current)
            current.pop()

    result = []
    quilui(1, [])
    return result


def main():
    while True:
        try:
            n = int(input("Nhập một số tự nhiên n (n < 1000): "))
            if 0 <= n < 1000:
                break
            else:
                print("n phải là số tự nhiên nhỏ hơn 1000.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    a = chuoi(n)

    print(f"\nCác tập con của tập {{1, 2, ..., {n}}}:")
    for i in a:
        print(i)
    print(f"\nTổng số tập con: {len(a)}")


if __name__ == "__main__":
    main()
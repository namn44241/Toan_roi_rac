# Liệt kê nghiệm nguyên của phương trình x1 + x2 + x3 = 15 với x1 ≥ 0 , x2 ≥ 0 , x3 ≥ 0.

def tao(a, b, c):
    if len(c) == b - 1:
        last_value = a - sum(c)
        if last_value >= 0:
            solutions.append(c + [last_value])
        return

    for i in range(a - sum(c) + 1):
        tao(a, b, c + [i])

def main():
    total = 15
    variables = 3
    global solutions
    solutions = []

    tao(total, variables, [])

    print(f"Các nghiệm nguyên không âm của phương trình x1 + x2 + x3 = {total}:")
    for n in solutions:
        print(f"x1 = {n[0]}, x2 = {n[1]}, x3 = {n[2]}")
    print(f"\nTổng số nghiệm: {len(solutions)}")

if __name__ == "__main__":
    main()
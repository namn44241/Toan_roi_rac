# Nhập 1 số nguyên dương N.
# In ra số nghiệm nguyên không âm của phương trình
# x1+x2+x3 = N

def count_non_negative_solutions(N):
    count = 0
    for x1 in range(N + 1):
        for x2 in range(N + 1):
            x3 = N - x1 - x2
            if x3 >= 0:
                count += 1
    return count

# Nhập số nguyên dương N từ người dùng
N = int(input("Nhập số nguyên dương N: "))
print("Số nghiệm nguyên không âm của phương trình x1 + x2 + x3 = N là:", count_non_negative_solutions(N))

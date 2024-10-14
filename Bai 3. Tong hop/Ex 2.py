# Nhập 1 số nguyên dương N.
# In ra số nghiệm nguyên không âm của phương trình
# x1+x2+x3 = N

def main(n):
    dem = 0
    for x1 in range(n + 1):
        for x2 in range(n + 1):
            x3 = n - x1 - x2
            if x3 >= 0:
                dem += 1
    return dem

# Nhập số nguyên dương N từ người dùng
N = int(input("Nhập số nguyên dương N: "))
print("Số nghiệm nguyên không âm của phương trình x1 + x2 + x3 = N là:", main(N))

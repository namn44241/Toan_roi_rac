def scs(n):
    if n == 0:
        return 0
    return 1 + scs(n // 10)
def tcs(n):
    if n ==0:
        return 0
    return n%10 + tcs(n//10)

def main():
    n = int(input("n:"))
    if 1 < n < 10**6:
        a = scs(n)
        b = tcs(n)
        print(f"scs {a}")
        print(f"tcs {b}")
    else:
        print('loi')
if __name__ == "__main__":
    main()

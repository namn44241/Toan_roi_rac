# Đếm các số không chia hết cho 2, 3, 5 trong khoảng từ 1 đến 1000 và tính tổng các số trên.

numbers = [i for i in range(1, 1001) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]
count = len(numbers)
total_sum = sum(numbers)

# In kết quả
print(f"Số lượng các số không chia hết cho 2, 3, 5 trong khoảng từ 1 đến 1000: {count}")
print(f"Tổng của các số đó: {total_sum}")
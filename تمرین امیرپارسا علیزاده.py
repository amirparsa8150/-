import random
import numpy as np

# کد ملی شما
code_melli = "0025359071"

# حذف تکرار ارقام
unique_digits = list(set(code_melli))
unique_digits = list(map(int, unique_digits))  # تبدیل به عدد صحیح

# ساخت ماتریس 10x10 با استفاده از اعداد بردار یکتا
matrix = []
for _ in range(10):
    row = random.choices(unique_digits, k=10)
    matrix.append(row)

# تبدیل به آرایه numpy برای نمایش بهتر
matrix_np = np.array(matrix)

# چاپ خروجی
print("بردار یکتا از کد ملی:", unique_digits)
print("ماتریس 10x10:")
print(matrix_np)
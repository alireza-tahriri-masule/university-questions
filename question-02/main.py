import matplotlib.pyplot as plt

# داده‌های X و Y
X = [2, 4, 6, 8, 10, 12, 14]
Y = [50, 100, 150, 200, 250, 300, 350]

# الف) رسم Scatter plot ساده
plt.scatter(X, Y)
plt.show()

# ب) پلات با داده‌های سبز و سایز کوچک
plt.scatter(X, Y, color='green', s=20)
plt.show()

# ج) پلات با داده‌های قرمز و سایز بزرگ
plt.scatter(X, Y, color='red', s=100)
plt.show()

# د) افزودن عنوان به محورها
plt.scatter(X, Y)
plt.xlabel("تعداد میوه‌ها")
plt.ylabel("قیمت")
plt.show()

# ه) تغییر سایز عنوان محورها
plt.scatter(X, Y)
plt.xlabel("تعداد میوه‌ها", fontsize=14)
plt.ylabel("قیمت", fontsize=14)
plt.show()

# ی) تغییر شکل داده‌ها، تغییر رنگ به بنفش، و اضافه کردن عنوان به نمودار
plt.scatter(X, Y, color='purple', s=100, marker='o')  # تغییر رنگ و شکل دایره‌ای
plt.xlabel("تعداد میوه‌ها", fontsize=14)
plt.ylabel("قیمت", fontsize=14)
plt.title("رابطه تعداد میوه با قیمت", loc='left')  # عنوان در بالا سمت چپ
plt.show()

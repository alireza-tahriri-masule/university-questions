import matplotlib.pyplot as plt

X = [2, 4, 6, 8, 10, 12, 14]
Y = [50, 100, 150, 200, 250, 300, 350]

plt.scatter(X, Y)
plt.show()

plt.scatter(X, Y, color='green', s=20)
plt.show()

plt.scatter(X, Y, color='red', s=100)
plt.show()

plt.scatter(X, Y)
plt.xlabel("تعداد میوه‌ها")
plt.ylabel("قیمت")
plt.show()

plt.scatter(X, Y)
plt.xlabel("تعداد میوه‌ها", fontsize=14)
plt.ylabel("قیمت", fontsize=14)
plt.show()

plt.scatter(X, Y, color='purple', s=100, marker='o') 
plt.xlabel("تعداد میوه‌ها", fontsize=14)
plt.ylabel("قیمت", fontsize=14)
plt.title("رابطه تعداد میوه با قیمت", loc='left')
plt.show()

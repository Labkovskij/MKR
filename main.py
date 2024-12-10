import numpy as np
import matplotlib.pyplot as plt

# Дані вибірки (змінити відповідно до завдання)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.2, 2.8, 3.6, 4.5, 5.1])

# Розрахунок параметрів моделі
n = len(x)
x_sum = np.sum(x)
y_sum = np.sum(y)
xy_sum = np.sum(x * y)
x_squared_sum = np.sum(x**2)

# Обчислення коефіцієнтів
a = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum**2)
b = (y_sum - a * x_sum) / n

# Генерація згладженої лінії
y_smooth = a * x + b

# Вивід результатів
print(f"Коефіцієнт a: {a}")
print(f"Коефіцієнт b: {b}")
print(f"Згладжені значення: {y_smooth}")

# Візуалізація результатів
plt.scatter(x, y, color='blue', label='Вихідні дані')
plt.plot(x, y_smooth, color='red', label='Згладжена лінія (МНК)')
plt.title('Згладжування методом найменших квадратів')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Створювати блукання, поки програма активна
while True:
    # Створити випадкове блукання
    rw = RandomWalk()
    rw.fill_walk()

    # Нанести на графік точки блукання
    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
               cmap=plt.cm.Blues, edgecolors='none', s=1)
    plt.show()

    # Виокремити першу та останню точки
    ax.scatter(0, 0, c='green', edgecolors='none', s=15)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)

    # Ховаємо осі
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    keep_running = input("Згенерувати нове блукання? (y/n): ")
    if keep_running == 'n':
        break
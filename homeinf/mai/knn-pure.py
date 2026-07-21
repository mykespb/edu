# Реализация KNN на чистом Python
# 2026-07-01 2026-07-01 1.0

from collections import Counter
import math


def euclidean_distance(point1, point2):
    """Считает Евклидово расстояние между двумя точками любой размерности."""
    squared_diff_sum = 0
    for i in range(len(point1)):
        # (x2 - x1)^2
        squared_diff_sum += (point2[i] - point1[i]) ** 2
    # Квадратный корень из суммы
    return math.sqrt(squared_diff_sum)


def predict_knn(X_train, y_train, new_point, k=3):
    """Предсказывает класс для новой точки на основе обучающей выборки."""
    distances = []

    # Шаг 1: Считаем расстояние от новой точки до ВСЕХ точек в базе данных
    for i in range(len(X_train)):
        dist = euclidean_distance(X_train[i], new_point)
        # Сохраняем пару: (расстояние, правильный ответ для этой точки)
        distances.append((dist, y_train[i]))

    # Шаг 2: Сортируем список по возрастанию расстояния (от самых близких к дальним)
    distances.sort(key=lambda x: x[0])

    # Шаг 3: Отбираем ровно K самых близких соседей
    k_nearest_neighbors = distances[:k]

    # Вытаскиваем только их классы (названия животных)
    k_nearest_labels = [label for dist, label in k_nearest_neighbors]

    # Печатаем для наглядности, кто оказался в соседях
    print(f"\nБлижайшие {k} соседа: {k_nearest_neighbors}")

    # Шаг 4: Голосование. Выбираем класс, который встречается чаще всего
    most_common = Counter(k_nearest_labels).most_common(1)

    # Возвращаем имя победившего класса
    return most_common[0][0]


# --- ПРОВЕРКА НА ПРАКТИКЕ ---

# Наша база данных животных (X - признаки, y - метки)
# Столбцы: [размер (0-2), уровень шума (0-2)]
X_train = [[0, 0], [1, 1], [1, 2], [1, 0], [0, 2], [2, 2], [2, 1]]

y_train = [
    "Хомяк",
    "Кошка",
    "Кошка",
    "Кошка",
    "Собака",
    "Собака",
    "Собака",
]

# Характеристики нового неизвестного животного
# Маленькое (0), но не самое тихое (1)
new_animal = [0, 1]

# Запускаем наше предсказание для K = 3
result = predict_knn(X_train, y_train, new_animal, k=3)

print(f"\nИтоговое предсказание алгоритма: {result}\n")

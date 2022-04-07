import os
import sys

from PIL import Image
import numpy as np

# Создание начальных точек для центроидов
def initialize_k_centroids(X, K):
    # Выбирается K поинты из Х по рандому
    m = len(X)
    return X[np.random.choice(m, K, replace=False), :]

# Определение функции для загрузки изображения, взятого в качестве параметра
def load_image(path):
    """ Загрузите изображение из пути """
    image = Image.open(path)
    return np.asarray(image) / 255
# Функция поиска центроида для каждого обучающего примера
def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)
    for i in range(m):
        # Нахождение расстояния
        distances = np.linalg.norm(X[i] - centroids, axis=1)
        # Назначение ближайшего кластер к c[i]
        c[i] = np.argmin(distances)
    return c
# Вычислить расстояние каждого примера до его центроида и взять среднее расстояние для каждого центроида
def compute_means(X, idx, K):
    _, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        examples = X[np.where(idx == k)]
        mean = [np.mean(column) for column in examples.T]
        centroids[k] = mean
    return centroids
# Установит максимальное количество итераций на 10. Если центроиды больше не двигаются, мы возвращаем результаты, поскольку мы не можем оптимизировать дальнейшую оптимизацию.
def find_k_means(X, K, max_iters=10):
    centroids = initialize_k_centroids(X, K)
    previous_centroids = centroids
    currentiteration = 0
    for _ in range(max_iters):
        currentiteration += 1
        print("Прогресс: ", (currentiteration / max_iters) * 100, "%")
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        if(centroids == previous_centroids).all():
            # Центроиды больше не двигаются
            return centroids
        else:
            previous_centroids = centroids
    return centroids, idx


def main():
    try:
        image_path = sys.argv[1]
        assert os.path.isfile(image_path)
    except (IndexError, AssertionError):
        print("Пожалуйста, укажите изображение")
    image = load_image(image_path)
    w, h, d = image.shape
    print("Изображено найдено с размером: {}, высота: {}, ширина: {}".format(w, h, d))

    # Мы изменяем форму изображения, потому что каждый пиксель имеет одинаковое значение (цвет), поэтому их не нужно представлять в виде сетки.
    X = image.reshape((w*h, d))
    K = 20  # Желаемое количество цветов в сжатом изображении

    # Цвета выбираются по алгоритму
    colors, _ = find_k_means(X, K, max_iters=10)
    # Вычисляются индексы текущих цветов
    print("Constructing compressed image")
    idx = find_closest_centroids(X, colors)

    # Когда у нас есть необходимые данные, мы реконструируем изображение, заменяя индекс цвета цветом и возвращая изображение к его исходному состоянию. Габаритные размеры
    idx = np.array(idx, dtype=np.uint8)
    X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
    compressed_image = Image.fromarray(X_reconstructed)
    compressed_image.save('compressed_image.jpg')
    print("Изображение создано")

if __name__ == "__main__":
    main()

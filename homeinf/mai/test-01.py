# ~ Studying  & testing AI K-nearest procedure.
# ~ 2026-06-29 2026-06-29 1.1.

# ~ from sklearn.neighbors import KNeighborsClassifier

# ~ types = ["Хомяк", "Кошка", "Собака"]
# ~ size = [0, 1, 2] # 0 - маленькое, 1 - среднее, 2 - большое
# ~ noize_level = [0, 1, 2] # 0 - тихое, 1 - не самое тихое, 2 - громкое

# ~ X = [[size[i], noize_level[i]] for i in range(len(types))]
# ~ y = types

# ~ model = KNeighborsClassifier(n_neighbors=1)
# ~ model.fit(X, y)

from sklearn.neighbors import KNeighborsClassifier

types = ["Хомяк", "Кошка", "Собака"]
size = [0, 1, 2] # 0 - маленькое, 1 - среднее, 2 - большое
noize_level = [0, 1, 2] # 0 - тихое, 1 - не самое тихое, 2 - громкое

X = [[size[i], noize_level[i]] for i in range(len(types))]
y = types

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)

new_size = 0
new_noize_level = 1

prediction = model.predict([[new_size, new_noize_level]])
print(f"Предсказание типа животного: {prediction[0]}")


# ~ myke@mykex:~/pro/edu/homeinf/mai$ uv run test-01.py 
# ~ Предсказание типа животного: Хомяк


# ~ Этот код обучает простую модель искусственного интеллекта распознавать тип животного по его размеру и уровню шума. Для этого используется алгоритм K-ближайших соседей (KNN).
# ~ Ниже представлен подробный разбор работы программы по шагам.
# ~ ## Подготовка данных

# ~ * Импорт: from sklearn.neighbors import KNeighborsClassifier загружает готовую модель классификации из библиотеки машинного обучения scikit-learn.
# ~ * База знаний (Классы): Массив types содержит целевые метки (ответы): Хомяк, Кошка, Собака.
# ~ * Признаки (Характеристики): Списки size и noize_level переводят текст в числа, так как алгоритмы работают только с цифрами.
# ~ * Хомяк = размер 0 (маленький), шум 0 (тихий).
   # ~ * Кошка = размер 1 (средний), шум 1 (не самый тихий).
   # ~ * Собака = размер 2 (большой), шум 2 (громкий).
# ~ * Формирование таблиц:
# ~ * Переменная X собирает пары признаков: [[0, 0], [1, 1], [2, 2]].
   # ~ * Переменная y хранит правильные ответы для этих пар: ["Хомяк", "Кошка", "Собака"].

# ~ ## Создание и обучение модели

# ~ * Инициализация: KNeighborsClassifier(n_neighbors=1) создает модель. Параметр n_neighbors=1 означает, что для классификации нового объекта модель будет искать ровно одного самого похожего «соседа» из обучающей выборки.
# ~ * Обучение: Метод model.fit(X, y) передает данные в модель. Она запоминает, какие характеристики соответствуют какому животному.

# ~ ## Предсказание для нового животного

# ~ * Вводятся характеристики неизвестного животного: new_size = 0 (маленькое) и new_noize_level = 1 (не самое тихое).
# ~ * Метод model.predict([[0, 1]]) сравнивает эту пару чисел с известными образцами.
# ~ * Геометрически точка [0, 1] находится ближе всего к точке хомяка [0, 0]. Поэтому модель выбирает его.
# ~ * Строка print выводит итоговый ответ в консоль: Предсказание типа животного: Хомяк.

# ~ ------------------------------
# ~ Если вы хотите развить этот пример, мы можем:

# ~ * Добавить новые характеристики (например, длину хвоста или количество шерсти).
# ~ * Посмотреть, как изменится ответ, если увеличить число соседей n_neighbors.
# ~ * Написать проверку точности модели на тестовых данных.

# ~ Какое направление вам интересно изучить подробнее?

# ~ uv add sklearn
# ~ Using CPython 3.14.2
# ~ Creating virtual environment at: .venv
  # ~ × Failed to build `sklearn==0.0.post12`
  # ~ ├─▶ The build backend returned an error
  # ~ ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)

      # ~ [stderr]
      # ~ The 'sklearn' PyPI package is deprecated, use 'scikit-learn'
      # ~ rather than 'sklearn' for pip commands.

      # ~ Here is how to fix this error in the main use cases:
      # ~ - use 'pip install scikit-learn' rather than 'pip install sklearn'
      # ~ - replace 'sklearn' by 'scikit-learn' in your pip requirements files
        # ~ (requirements.txt, setup.py, setup.cfg, Pipfile, etc ...)
      # ~ - if the 'sklearn' package is used by one of your dependencies,
        # ~ it would be great if you take some time to track which package uses
        # ~ 'sklearn' instead of 'scikit-learn' and report it to their issue tracker
      # ~ - as a last resort, set the environment variable
        # ~ SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True to avoid this error

      # ~ More information is available at
      # ~ https://github.com/scikit-learn/sklearn-pypi-package


# ~ hint: `sklearn` is often confused for `scikit-learn`. Did you mean to install `scikit-learn` instead?
# ~ hint: Build failures usually indicate a problem with the package or the build environment
# ~ hint: If you want to add the package regardless of the failed resolution, provide the `--frozen` flag to skip locking and syncing
# ~ myke@mykex:~/pro/edu/homeinf/ai$ uv run test-01.py 
# ~ Traceback (most recent call last):
  # ~ File "/home/myke/pro/edu/homeinf/ai/test-01.py", line 1, in <module>
    # ~ from sklearn.neighbors import KNeighborsClassifier
# ~ ModuleNotFoundError: No module named 'sklearn'

# ~ $ uv add scikit-learn
# ~ Resolved 7 packages in 920ms
# ~ Prepared 6 packages in 30.48s
# ~ Installed 6 packages in 19ms
 # ~ + joblib==1.5.3
 # ~ + narwhals==2.22.1
 # ~ + numpy==2.5.0
 # ~ + scikit-learn==1.9.0
 # ~ + scipy==1.18.0
 # ~ + threadpoolctl==3.6.0

# ~ myke@mykex:~/pro/edu/homeinf/mai$ uv tree
# ~ Resolved 7 packages in 0.65ms
# ~ ai v0.1.0
# ~ └── scikit-learn v1.9.0
    # ~ ├── joblib v1.5.3
    # ~ ├── narwhals v2.22.1
    # ~ ├── numpy v2.5.0
    # ~ ├── scipy v1.18.0
    # ~ │   └── numpy v2.5.0
    # ~ └── threadpoolctl v3.6.0

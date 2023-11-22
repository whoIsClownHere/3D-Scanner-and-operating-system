import random

diametre_platform = 10
platform_object_gap = 10

# угол поворота платформы в градусах
platform_rotation_angle = 2
# всего градусов при повороте в градусах
total_rotation_angle = 360

len_of_one_height = int(total_rotation_angle / platform_rotation_angle)

# делаем сложную форму фигуры
first_distance = 13
distances = [first_distance]

for i in range(int(total_rotation_angle / platform_rotation_angle)):
    last_element = distances[-1]

    # Генерируем шум, который плавно переходит к начальному значению
    noise = (1 - i / len_of_one_height) * last_element + (i / len_of_one_height) * first_distance

    # Убедимся, что шум не отличается от соседнего на 0.1
    if i > 0:
        while abs(noise - distances[-1]) < 0.1:
            noise += random.uniform(-0.1, 0.1)

    distances.append(noise)

# Убедимся, что первый и последний элементы равны
distances[-1] = first_distance

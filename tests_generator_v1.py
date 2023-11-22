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

    noise = last_element + random.uniform(-0.3, 0.3)
    if noise >= (diametre_platform + platform_object_gap):
        distances.append(last_element - 0.1)
    elif noise <= platform_object_gap:
        distances.append(last_element + 0.1)
    else:
        distances.append(last_element + random.uniform(-0.1, 0.1))

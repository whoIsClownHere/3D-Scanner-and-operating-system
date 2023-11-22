import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns

# угол поворота платформы в градусах
platform_rotation_angle = 2
# всего градусов при повороте в градусах
total_rotation_angle = 360

len_of_one_height = int(total_rotation_angle / platform_rotation_angle)

diametre_platform = 10
platform_object_gap = 10


def converting_distance_to_coordinates(data):
  data_x = []
  data_y = []
  
  for i in range(int(total_rotation_angle / platform_rotation_angle)):
      index_distance = (data[i] - diametre_platform / 2 - platform_object_gap)
      
      engle = i * platform_rotation_angle
      engle_sin = np.sin(engle * np.pi / 180. )
      engle_cos = np.cos(engle * np.pi / 180. )
  
      data_y.append(index_distance * engle_sin)
      data_x.append(index_distance * engle_cos)


def interpolate_data(data, scale_ratio=4, kind=2):
    data = np.array(data)
    data_linspace = np.linspace(0, 10, num=len(data), endpoint=True)
     
    f = interp1d(data_linspace, data, kind=kind)
    x_new = np.linspace(0, 10, num=(len(data) * scale_ratio), endpoint=True)
    y_new = f(x_new)
    
    return y_new, x_new, data_linspace


import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import radar

def recalculate_spherical(deltaX, deltaY, deltaZ, deltaT, x, y, z):
  # this function converts derivatives from cartestian to spherical coordinates
  dtheta_dt  = (-x / ((x ** 2) + (y ** 2)) ) * (deltaX) + (x / ((x ** 2) + (y ** 2)) ) * (deltaY)
  dphi_dt = ((z * x_two) / (sqrt(x ** 2 + y **2) * (x ** 2 + z **2 + y **2))) * (deltaX)  + ((z * x) / (sqrt(x ** 2 + y **2) * (x ** 2 + z **2 + y **2))) * (deltaY) - (sqrt(y ** 2 + x ** 2) / (z ** 2 + x **2 + y **2 )) * deltaZ
  dp_dt = (x / sqrt (x ** 2 + y ** 2 + z ** 2)) * deltaX + (y / sqrt(x ** 2 + y ** 2  + z **2)) * deltaY + (z / sqrt(x ** 2 + y ** 2  + z **2)) * deltaZ 
  return [dtheta_dt, dphi_dt, dp_dt]

def calculate_ballistics_missile(speed, phi, theta):
  # this calculates the cartestian vector of the missile from launch
  # makes solving differential equation easier
  # this function is also used in ballistics sim as it uses it own origin as reference for phi and theta
  
  deltaX = (speed) * (np.cos(theta)) * (np.sin(phi))
  deltaY = (speed) * (np.sin(theta)) * (np.sin(phi))
  deltaZ = (speed) * (np.cos(phi))
  deltaXYZ = [deltaX, deltaY, deltaZ]
  return deltaXYZ

def laser_solution(x, deltaXYZ, xyz_two, missile_speed):
  # x0 is time, x1 is phi, x2 is theta, 
  # this is the function used by scipy to solve as a set of three equations 
  m_x_speed, m_y_speed, m_z_speed = calculate_ballistics_missile(missile_speed, x[1], x[2])
  t_x_speed, t_y_speed, t_z_speed = deltaXYZ
  t_x_pos, t_y_pos, t_z_pos = xyz_two
  return [0 + m_x_speed * x[0] - t_x_pos - (t_x_speed) * x[0], 0 + m_y_speed * x[0] - t_y_pos - (t_y_speed) * x[0], 0 + m_z_speed * x[0] - t_z_pos - (t_z_speed) * x[0]]

# Commenting Out until Laser is Fixed

# def proj_solution(x, deltaXYZ, xyz_two, missile_speed):
#   # this is the function assuming the projectile is affected by gravity 
  
#   # x0 is time, x1 is phi, x2 is theta, 
#   # this is the function used by scipy to solve as a set of three equations 
#   m_x_speed, m_y_speed, m_z_speed = calculate_ballistics_missile(missile_speed, x[1], x[2])
#   t_x_speed, t_y_speed, t_z_speed = deltaXYZ
#   t_x_pos, t_y_pos, t_z_pos = xyz_two
#   return [0 + m_x_speed * x[0] - t_x_pos - (t_x_speed) * x[0], 0 + m_y_speed * x[0] - t_y_pos - (t_y_speed) * x[0], 0 + m_z_speed * x[0] - (0.5 * 9.81 * (x[0] ** 2)) - t_z_pos - (t_z_speed) * x[0]]


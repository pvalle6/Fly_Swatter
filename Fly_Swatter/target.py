import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import radar

def calculate_trajectory_target(first_data, second_data):
  # probably want to convert to cartesian coordinates immedatiately unless there is a spherical coordinate formula

  x_one = (first_data.r) * (np.cos(first_data.theta)) * (np.sin(first_data.phi))
  y_one = (first_data.r) * (np.sin(first_data.theta)) * (np.sin(first_data.phi))
  z_one = (first_data.r) * (np.cos(first_data.phi))

  x_two = (second_data.r) * (np.cos(second_data.theta)) * (np.sin(second_data.phi))
  y_two = (second_data.r) * (np.sin(second_data.theta)) * (np.sin(second_data.phi))
  z_two = (second_data.r) * (np.cos(second_data.phi))

  xyz_one = [x_one,y_one,y_two]
  xyz_two  = [x_two, y_two, z_two]

  deltaT = second_data.time_spot - first_data.time_spot 

  deltaX = (x_two - x_one) / deltaT
  deltaY = (y_two - y_one) / deltaT
  deltaZ = (z_two - z_one) / deltaT

  deltaXYZ = [deltaX, deltaY, deltaZ]

  return [deltaT, deltaXYZ, xyz_one, xyz_two]

def recalculate_spherical(deltaX, deltaY, deltaZ, deltaT, x, y, z):

  dtheta_dt  = (-x / ((x ** 2) + (y ** 2)) ) * (deltaX) + (x / ((x ** 2) + (y ** 2)) ) * (deltaY)
  dphi_dt = ((z * x_two) / (sqrt(x ** 2 + y **2) * (x ** 2 + z **2 + y **2))) * (deltaX)  + ((z * x) / (sqrt(x ** 2 + y **2) * (x ** 2 + z **2 + y **2))) * (deltaY) - (sqrt(y ** 2 + x ** 2) / (z ** 2 + x **2 + y **2 )) * deltaZ
  dp_dt = (x / sqrt (x ** 2 + y ** 2 + z ** 2)) * deltaX + (y / sqrt(x ** 2 + y ** 2  + z **2)) * deltaY + (z / sqrt(x ** 2 + y ** 2  + z **2)) * deltaZ 
  return [dtheta_dt, dphi_dt, dp_dt]

def calculate_ballistics_missile(speed, phi, theta):
  # probably want to convert to cartesian coordinates immedatiately unless there is a spherical coordinate formula

  deltaX = (speed) * (np.cos(theta)) * (np.sin(phi))
  deltaY = (speed) * (np.sin(theta)) * (np.sin(phi))
  deltaZ = (speed) * (np.cos(phi))
  deltaXYZ = [deltaX, deltaY, deltaZ]
  return deltaXYZ

def find_firing_solution(x, deltaXYZ, xyz_two, missile_speed):
  # x0 is time, x1 is theta, x2 is phi
  m_x_speed, m_y_speed, m_z_speed = calculate_ballistics_missile(missile_speed, x[2], x[1])
  t_x_speed, t_y_speed, t_z_speed = deltaXYZ
  t_x_pos, t_y_pos, t_z_pos = xyz_two
  return [0 + m_x_speed * x[0] - t_x_pos - (t_x_speed) * x[0], 0 + m_y_speed * x[0] - t_y_pos - (t_y_speed) * x[0], 0 + m_z_speed * x[0] - t_z_pos - (t_z_speed) * x[0]]

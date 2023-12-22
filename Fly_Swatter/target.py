import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import radar

# def recalculate_spherical(deltaX, deltaY, deltaZ, deltaT, x, y, z):
 # """ Converts Cartesian Coordinates to Spherical Coordinates """
#   # this function converts derivatives from cartestian to spherical coordinates
#   dtheta_dt  = (-x / ((x ** 2) + (y ** 2)) ) * (deltaX) + (x / ((x ** 2) + (y ** 2)) ) * (deltaY)
#   dphi_dt = ((z * x_two) / (sqrt(x ** 2 + y **2) * (x ** 2 + z **2 + y **2))) * (deltaX)  + ((z * x) / (sqrt(x ** 2 + y **2) * (x ** 2 + z **2 + y **2))) * (deltaY) - (sqrt(y ** 2 + x ** 2) / (z ** 2 + x **2 + y **2 )) * deltaZ
#   dp_dt = (x / sqrt (x ** 2 + y ** 2 + z ** 2)) * deltaX + (y / sqrt(x ** 2 + y ** 2  + z **2)) * deltaY + (z / sqrt(x ** 2 + y ** 2  + z **2)) * deltaZ 
#   return [dtheta_dt, dphi_dt, dp_dt]

def calculate_ballistics_missile(speed, phi, theta):
  """ Converts Spherical Coordinates to Cartesian Coordinates
     speed: rho or any straight-line distance 
     phi is the angle as measured from top to bottom of the z-axis
     theta is the angle as measured around the z-axis
  """
  
  deltaX = (speed) * (np.cos(theta)) * (np.sin(phi))
  deltaY = (speed) * (np.sin(theta)) * (np.sin(phi))
  deltaZ = (speed) * (np.cos(phi))
  deltaXYZ = [deltaX, deltaY, deltaZ]
  return deltaXYZ

def laser_solution(x, deltaXYZ, xyz_two, missile_speed):
  """ provides the function to the equation solver for a laser solution without gravity or air
      x: is the solution to be solved for 
      deltaXYZ: is the change in speed components in cartestian coordinates of the target 
      xyz_two: is the second "pinged" location of the target
      missile_speed: constant speed of laser
  """
  m_x_speed, m_y_speed, m_z_speed = calculate_ballistics_missile(missile_speed, x[1], x[2])
  t_x_speed, t_y_speed, t_z_speed = deltaXYZ
  t_x_pos, t_y_pos, t_z_pos = xyz_two
  return [0 + m_x_speed * x[0] - t_x_pos - (t_x_speed) * x[0], 0 + m_y_speed * x[0] - t_y_pos - (t_y_speed) * x[0], 0 + m_z_speed * x[0] - t_z_pos - (t_z_speed) * x[0]]

# Commenting Out until Laser is Fixed

def proj_solution(x, deltaXYZ, xyz_two, missile_speed):
  """ provides the function to the equation solver for a ballistic solution with gravity and without air
      x: is the solution to be solved for 
      deltaXYZ: is the change in speed components in cartestian coordinates of the target 
      xyz_two: is the second "pinged" location of the target
      missile_speed: constant speed of projectile
  """
  m_x_speed, m_y_speed, m_z_speed = calculate_ballistics_missile(missile_speed, x[1], x[2])
  t_x_speed, t_y_speed, t_z_speed = deltaXYZ
  t_x_pos, t_y_pos, t_z_pos = xyz_two
  return [0 + m_x_speed * x[0] - t_x_pos - (t_x_speed) * x[0], 0 + m_y_speed * x[0] - t_y_pos - (t_y_speed) * x[0], 0 + m_z_speed * x[0] - (0.5 * 9.81 * (x[0] ** 2)) - t_z_pos - (t_z_speed) * x[0]]


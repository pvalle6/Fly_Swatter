import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target

class ballistic():
  def __init__(self, name, btype, status, theta, phi, x, y, z, speed):
    # initiallization should be considered the initial position and velocity of the object
    # again it should be noted that theta and phi are not in refernece to the origin but to the angle at which the object is continuing
    self.name = name
    self.btype = btype
    self.status = status
    self.theta = theta
    self.phi = phi
    self.x = x
    self.y = y
    self.z = z
    self.speed = speed
    self.life_time = time.time() # relatively zero, absolutely to unix
  def get_loc_speed(time_sample):
    if self.btype == "simple_kin":
      # this option should use the kinematic equations and unix time to calculate the trajectory and return locations and velocity vectors
    else:
      # Runge Kutta Hell
      # I haven't put air resistance
      # I also could merge and implement straight line kinematics in here or continuous flights

    


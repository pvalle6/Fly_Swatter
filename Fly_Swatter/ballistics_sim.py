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


import numpy as np
import scipy
import time
import sched
import random
# to calculate the ballistics of a target, two samples is the minimum required for a triangle to be created

# simple example assumes a sonar image (probably want to generalize this to radar or image recognition)
class target_loc():
  # this class controls the 3D position and recording of radar data
  def __init__(self, phi, theta, r, time_spot):
    self.phi = phi
    self.theta = theta
    self.r = r
    self.time_spot = time_spot
  def tell(self):
    return (f"Phi: {self.phi}  " + f"Theta: {self.theta} " + f"Rho: {self.r}")

def target_radar_sight(return_data):
  # need a function that captures a location of the target
  time = time.time()
  return phi, theta, r, time

# code to generate random vector of target
# self, phi, theta, r, time_spot)
def generate_random_vector(max_distance, speed):
  # this generates a simulation of the radar data given parameters
  # this program is entirely from the POV of the launch system in terms of phi, theta, distance, and speed

  phi = random.randrange(0,10, 1) * (np.pi / 2) / 10 # bounds of phi are 0 to pi / 2
  theta = random.randrange(-10,10, 1) * (np.pi / 2) / 10 # important to note that the bounds of theta are - pi/2 to pi/2

  data_one = target_loc(phi, theta, max_distance, 0)
  # need to update this to create more randomized velocity vectors for simulated targets 
  # as it currently exsits, the difference is small but it seems that small changes can cause radical differences in the spherical coordinate system
  
  data_two = target_loc(phi + 0.01,theta + 0.01, max_distance + 0.01, 0.1)

  return [data_one, data_two]

def generate_parabolic_vector(max_distance):
  # only the intial vector is supplied by this, the actual course needs to be simulated by a differential equation solver
  # assuming launcher sytem is located at (0,0,0)

  # should be noted that though generated_random_vector uses phi and theta in terms of the launch system,
  # the phi and theta referenced here are from the perspective of the initial site
  
  # note that this random angle has nothing to do with theta or phi, it is just a simple way of generating a set of x and y coordinates
  random_ground_angle = random.randrange(-10,10, 1) * (np.pi / 2) / 10
  z = 0
  y = max_distance * np.sin(random_angle)
  x = max_distance * np.cos(random_angle)

  # i want this to be mortar like, so phi needs to be quite large, theta probably should be towards (0,0,0) with some deviation
  phi = random.randrange(3,10, 1) * (np.pi / 2) / 10 # bounds of phi are 0 to pi / 2
  # to make a theta that is pointed somewhat towards origin, with a little deviation
  theta = np.tan(y/x) + (random.randrange(-10,10)/50)
  
  v_naught = 2
  initial_xyz = [x,y,z]
  
  return [initial_xyz, v_naught, phi, theta]

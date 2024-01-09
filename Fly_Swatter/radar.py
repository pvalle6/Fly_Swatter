import numpy as np
import scipy
import time
import sched
import random
# to calculate the ballistics of a target, two samples is the minimum required for a triangle to be created

# simple example assumes a sonar image (probably want to generalize this to radar or image recognition)
class target_loc():
  """ Class for a target location as found/generated from origin """
  # this class controls the 3D position and recording of radar data
  def __init__(self, phi, theta, r, time_spot):
    self.phi = phi
    self.theta = theta
    self.r = r
    self.time_spot = time_spot
  def tell(self):
    return (f"Phi: {self.phi}  " + f"Theta: {self.theta} " + f"Rho: {self.r}")

class velocity_vector():
  """Class for holding the velocity vector of a target"""
  def __init__(self, phi, theta, speed):
    # phi and theta are in relation to the target and not the radar origin
    self.phi_d = phi
    self.theta_d = theta
    self.speed_d = speed

class contact_database():
  """ Class for Holding the Contact Data """
  def __init__(self, name, contacts):
    self.name = name
    self.contacts = contacts
  def add_contact(self, new_contact):
    self.contacts.append(new_contact)
  def list_contacts(self):
    return_list = []
    for i in self.contacts:
      return_list.append(i.name)
    return return_list
      

class contact():
  """ Class for a contact """
  def __init__(self, name, last_time, last_loc, vel_vector, status):
    self.name = name
    self.last_time = last_time
    self.last_loc = last_loc
    self.status = status
    self.velocity = vel_vector
  def change_name(self, new_name):
    self.name = new_name
  def update_loc(self, last_loc, last_time):
    self.last_loc = last_loc
    self.last_time = last_time
  def update_status(self, new_status):
    self.status = new_status


def generate_random_vector(seed = None):
  """ Generates a random spherical coordinate given Rho = max_distance and a speed of the projectile """
  # probably need to wrap this into a difference set of functions as well as calculate trajectory target 
  # need to remove speed from here as well as the provided parametrs when this is used 
  
  random.seed(seed)
  distance = random.random() * 8 + 1
  
  phi = (random.randrange(0,8) * (np.pi / 2) / 10) + 0.1 # bounds of phi are 0 to pi / 2
  theta = random.randrange(-10,10) * (np.pi / 2) / 10 # important to note that the bounds of theta are - pi/2 to pi/2
  first_data = target_loc(phi = phi, r = distance, theta = theta, time_spot = time.time())
  return first_data

def generate_random_velocity(seed = None):

  if seed != None:
    seed_two = seed ** 2
  else:
    seed_two = None
  random.seed(seed_two)
  speed = random.random() *  1

  phi = (random.randrange(0,8) * (np.pi / 2) / 10) + 0.1 # bounds of phi are 0 to pi / 2
  theta = random.randrange(-10,10) * (np.pi / 2) / 10 # important to note that the bounds of theta are - pi/2 to pi/2

  velocity = velocity_vector(speed = speed, phi = phi, theta = theta)
  return velocity

def calculate_trajectory_target(last_loc, velocity):
  """ Generates a random second location of a randomly generated projectile and its velocity vector"""
  # need to create a integrated version of this and gneerate random vector

  x_one = (last_loc.r) * (np.cos(last_loc.theta)) * (np.sin(last_loc.phi))
  y_one = (last_loc.r) * (np.sin(last_loc.theta)) * (np.sin(last_loc.phi))
  z_one = (last_loc.r) * (np.cos(last_loc.phi))
  
  xyz_one = [x_one,y_one, z_one]

  #deltaT = second_data.time_spot - first_data.time_spot 
  deltaT = 1
  deltaX = (velocity.speed_d) * (np.cos(velocity.theta_d)) * (np.sin(velocity.phi_d))
  deltaY = (velocity.speed_d) * (np.sin(velocity.theta_d)) * (np.sin(velocity.phi_d))
  deltaZ = (velocity.speed_d) * (np.cos(velocity.phi_d))

  deltaXYZ = [deltaX, deltaY, deltaZ]

  return [deltaT, deltaXYZ, xyz_one]

# def generate_parabolic_vector(max_distance):
#   # only the intial vector is supplied by this, the actual course needs to be simulated by a differential equation solver
#   # assuming launcher sytem is located at (0,0,0)

#   # should be noted that though generated_random_vector uses phi and theta in terms of the launch system,
#   # the phi and theta referenced here are from the perspective of the initial site
  
#   # note that this random angle has nothing to do with theta or phi, it is just a simple way of generating a set of x and y coordinates
#   random_ground_angle = random.randrange(-10,10, 1) * (np.pi / 2) / 10
#   z = 0
#   y = max_distance * np.sin(random_angle)
#   x = max_distance * np.cos(random_angle)

#   # i want this to be mortar like, so phi needs to be quite large, theta probably should be towards (0,0,0) with some deviation
#   phi = random.randrange(3,10, 1) * (np.pi / 2) / 10 # bounds of phi are 0 to pi / 2
#   # to make a theta that is pointed somewhat towards origin, with a little deviation
#   theta = np.tan(y/x) + (random.randrange(-10,10)/50)
  
#   v_naught = 2
#   initial_xyz = [x,y,z]
  
#   return [initial_xyz, v_naught, phi, theta]

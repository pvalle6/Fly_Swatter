import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target
from Fly_Swatter.Fly_Swatter import graph_trajectory

def check_valdity(solution):
  """ Checks if the solution could plausibily occur (negative time are just blips in the solution calculator) """
  if solution[0] <= 0.05:
    return False
  else:
    return True

def laser_handler(contact, missile_speed = 10):
  """ function for handling the calculation of a laser based interception """
  deltaT, deltaXYZ, xyz_one = radar.calculate_trajectory_target(contact.last_loc, contact.velocity)
  guess_solution = xyz_one
  solution = scipy.optimize.fsolve(target.laser_solution, guess_solution, args=(deltaXYZ, xyz_one, missile_speed))
  if(check_valdity(solution)):
    return [solution, True, deltaXYZ, xyz_one, missile_speed]
  else:
    return [None, False, None, None, None]
    
def grav_handler(contact, missile_speed = 10):
  """ function for handling the calculation of a gravity based ballistic interception """
  deltaT, deltaXYZ, xyz_one = radar.calculate_trajectory_target(contact.last_loc, contact.velocity)
  guess_solution = xyz_one
  solution = scipy.optimize.fsolve(target.proj_solution, guess_solution, args=(deltaXYZ, xyz_one, missile_speed))
  if(check_valdity(solution)):
    return [solution, True, deltaXYZ, xyz_one, missile_speed]
  else:
    return [None, False, None, None, None]
  
def track_lock(contact, projectile_type = 0, target_course: str = "straight"):
  """ Main function for calculating and handling the different  targeting solutions for fire_mode"""
  if projectile_type == 0 and target_course == "straight":
    validity = False
    print("SOLUTION INCOMING \n")
    solution, validity, deltaXYZ, xyz_one, missile_speed = laser_handler(contact)
    if validity:
      log = [solution, deltaXYZ, xyz_one, missile_speed]
    else:
      print("NO SOLUTION YET AVALIABLE, INVALID AZMIMUTH")
      log = [[None,None,None], None, None, None]

  elif projectile_type == 1 and target_course == "straight":
     print("SOLUTION INCOMING \n")

     solution, validity, deltaXYZ, xyz_one, missile_speed = grav_handler(contact)
     if validity:
       log = [solution, deltaXYZ, xyz_one, missile_speed]
     else:
       log = [[None,None,None], None, None, None]
  else:
    print("NO SOLUTION YET AVALIABLE, OUT OF BOUNDS")
    log = log = [[None,None,None], None, None, None]
  return log
  


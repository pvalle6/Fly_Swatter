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

def laser_handler(first_loc, seed = None, missile_speed = 10):
  """ function for handling the calculation of a laser based interception """
  deltaT, deltaXYZ, xyz_one, xyz_two = radar.calculate_trajectory_target(first_loc, seed)
  guess_solution = xyz_two
  solution = scipy.optimize.fsolve(target.laser_solution, guess_solution, args=(deltaXYZ, xyz_two, missile_speed))
  if(check_valdity(solution)):
    return [solution, True, deltaXYZ, xyz_two, missile_speed]
  else:
    return [None, False, None, None, None]
    
def grav_handler(first_loc, seed = None, missile_speed = 10):
  """ function for handling the calculation of a gravity based ballistic interception """
  deltaT, deltaXYZ, xyz_one, xyz_two = radar.calculate_trajectory_target(first_loc, seed)
  guess_solution = xyz_two
  solution = scipy.optimize.fsolve(target.proj_solution, guess_solution, args=(deltaXYZ, xyz_two, missile_speed))
  if(check_valdity(solution)):
    return [solution, True, deltaXYZ, xyz_two, missile_speed]
  else:
    return [None, False, None, None, None]
  
def track_lock(first_loc, realism = 0, projectile_type = "bullet", target_course = "straight", seed = None):
 """ Main function for calculating and handling the different  targeting solutions for fire_mode"""
  if realism == 0 and projectile_type == "bullet" and target_course == "straight":
    validity = False
    print("SOLUTION INCOMING \n")
    

    solution, validity, deltaXYZ, xyzTwo, missile_speed = laser_handler(first_loc, seed = seed)
    if validity:
      log = [solution, deltaXYZ, xyzTwo, missile_speed]
    else:
      # print("NO SOLUTION YET AVALIABLE, INVALID AZMIMUTH")
      log = ("FIRING SOLUTION RESULTS: \n") + (f"REAL TIME: {time.time()}" + "NO SOLUTION YET AVALIABLE, INVALID AZMIMUTH")
  else:
      # print("NO SOLUTION YET AVALIABLE, OUT OF BOUNDS")
      log = ("FIRING SOLUTION RESULTS: \n")+ (f"REAL TIME: {time.time()}" + "NO SOLUTION YET AVALIABLE, OUT OF BOUNDS")
  if realism == 1 and projectile_type == "bullet" and target_course == "straight":
     print("SOLUTION INCOMING \n")
     first_loc = radar.generate_random_vector(2, 2, seed)
     solution, validity, deltaXYZ, xyzTwo, missile_speed = grav_handler(first_loc, seed = seed)
     if validity:
       log = [solution, deltaXYZ, xyzTwo, missile_speed]
  return log
  


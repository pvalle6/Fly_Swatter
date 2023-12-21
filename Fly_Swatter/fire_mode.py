import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target
from Fly_Swatter.Fly_Swatter import graph_trajectory

def check_valdity(solution):
  if solution[0] <= 0.05:
    return False
  else:
    return True

def laser_handler(first_loc, seed = None, missile_speed = 10):

  deltaT, deltaXYZ, xyz_one, xyz_two = radar.calculate_trajectory_target(first_loc, seed)
  guess_solution = xyz_two
  solution = scipy.optimize.fsolve(target.laser_solution, guess_solution, args=(deltaXYZ, xyz_two, missile_speed))
  if(check_valdity(solution)):
    return [solution, True, deltaXYZ, xyz_two, missile_speed]
  else:
    return [None, False, None, None]
    
  def grav_handler(first_loc, seed = None, missile_speed = 10):
    deltaT, deltaXYZ, xyz_one, xyz_two = radar.calculate_trajectory_target(first_loc, seed)
    guess_solution = xyz_two
    solution = scipy.optimize.fsolve(target.proj_solution, guess_solution, args=(deltaXYZ, xyz_two, missile_speed))
    if(check_valdity(solution)):
      return [solution, True, deltaXYZ, xyz_two, missile_speed]
    else:
      return [None, False, None, None]
  
def track_lock(realism = 0, projectile_type = "bullet", target_course = "straight", seed = None, graphical = False):
 # three realism levels to calculate for 
  if realism == 0 and projectile_type == "bullet" and target_course == "straight":
    validity = False
    print("SOLUTION INCOMING \n")
    first_loc = radar.generate_random_vector(2, 2, seed)

    solution, validity, deltaXYZ, xyzTwo, missile_speed = laser_handler(first_loc, seed = seed)
    if validity:
      if graphical:
          graph_trajectory.graph_solution(missile_speed, solution[1], solution[2], deltaXYZ, xyzTwo, solution[0])
      log = ("FIRING SOLUTION RESULTS: \n") + (f"REAL TIME: {time.time()} \n" + (f"Time to Target: {solution[0]}\nPhi to Target: {solution[1]}\nTheta to Target: {solution[2]}"))
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
      log = ("FIRING SOLUTION RESULTS: \n") + (f"REAL TIME: {time.time()} \n" + (f"Time to Target: {solution[0]}\nPhi to Target: {solution[1]}\nTheta to Target: {solution[2]}"))
  return log
  


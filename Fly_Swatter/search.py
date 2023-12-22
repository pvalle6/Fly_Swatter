import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import search
from Fly_Swatter.Fly_Swatter import fire_mode
from Fly_Swatter.Fly_Swatter import target
from Fly_Swatter.Fly_Swatter import graph_trajectory

def target_check(image = None, search_seed = None, fire_seed = None):
  """ Provides a simulation of detecting a airbourne target
      image: default = none, this is just a placeholder for image/radar detection
      seed: default = none, this is provided through mode_control, and used in probability calculation; 10 returns True always
  """
  # seed = 10 returns True always
  random.seed(search_seed)
  # is recognized 
  # to simulate, roll die with 1/10 probability
  if random.randint(1,10) > 9:
    first_loc = radar.generate_random_vector(seed = fire_seed)
    return [True, first_loc]
  else:
    return [False, None]
  
def search_mode(runs = 10, seed_fire = None, seed_search = None):
  """ provides for a scheduling of a scanning event to simulate a radar search
      runs: default = 10, this provides how many runs and probabilities should be calculated until something is found or retiring
      seed: default = none, this is provided through mode_control and is used in target_check, and used in probability calculation; 10 returns True always
  """
  scheduler = sched.scheduler(time.time, time.sleep)
  
  search = True
  rotation_count = 0 
  
  target_mode = False
  while search:
    rotation_count = rotation_count + 1
    scheduler.enter(1,1, print, ("SCANNING"))
    scheduler.run()
    ping, first_loc = target_check(image = None, search_seed = seed_search, fire_seed = seed_fire)
    if ping:
      search = False
      print("TARGET SPOTTED")
      return [True, first_loc] 
    else:
      if rotation_count >= runs:
        search = False
        return [False, None]
      #rotate(phi, theta)

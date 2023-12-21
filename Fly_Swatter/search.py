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

def target_check(image = None, seed = None):
  # seed = 10 returns True always
  random.seed(seed)
  # is recognized 
  # to simulate, roll die with 1/10 probability
  if random.randint(1,10) > 9:
    return True
  else:
    return False
  
def search_mode(runs = 10, seed = None):
  # this needs to create a scheduled series of events and a quick break once a target is identified 
  # should schedule a scan and recoding of event, maybe implement a saving of initial target location
  scheduler = sched.scheduler(time.time, time.sleep)
  
  search = True
  rotation_count = 0 
  
  target_mode = False
  while search:
    rotation_count = rotation_count + 1
    scheduler.enter(1,1, print, ("SCANNING"))
    scheduler.run()

    if target_check(seed):
      search = False
      print("TARGET SPOTTED")
      return True
    else:
      if rotation_count >= runs:
        search = False
        return False
      #rotate(phi, theta)

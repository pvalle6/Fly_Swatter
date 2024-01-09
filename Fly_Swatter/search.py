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

def target_check(search_seed: int = None, fire_seed: int = None):
  """ Provides a simulation of detecting a airbourne target
      image: default = none, this is just a placeholder for image/radar detection
      seed: default = none, this is provided through mode_control, and used in probability calculation; 10 returns True always
  """
  # seed = 10 returns True always
  random.seed(search_seed)
  # is recognized 
  # to simulate, roll die with 1/10 probability
  if random.randint(1,10) > 7:
    first_loc = radar.generate_random_vector(seed = fire_seed)
    velocity = radar.generate_random_velocity(seed = fire_seed)
    return [True, first_loc, velocity]
  else:
    return [False, None, None]
  
def search_mode(runs: int = 10, seed_fire: int = None, seed_search: int = None):
  """ provides for a scheduling of a scanning event to simulate a radar search
      runs: default = 10, this provides how many runs and probabilities should be calculated until something is found or retiring
      seed: default = none, this is provided through mode_control and is used in target_check, and used in probability calculation; 10 returns True always
  """
  scheduler = sched.scheduler(time.time, time.sleep)
  return_log = [False, []]
  search = True
  rotation_count = 0 
  
  target_mode = False
  
  id = 0
  contact_database = radar.contact_database("Main_R", [])
  while search:
    rotation_count = rotation_count + 1
    scheduler.enter(1,1, print, ("SCANNING"))
    scheduler.run()
    ping, first_loc, velocity = target_check(search_seed = seed_search, fire_seed = seed_fire)
    
    if ping:
      print("TARGET SPOTTED")
      con_ = radar.contact(name = f"UN {id}", last_time = time.time(), last_loc = first_loc, vel_vector = velocity, status = "UN")
      id = id + 1
      contact_database.contacts.append(con_)
      print(contact_database.contacts)
    if rotation_count >= runs:
      search = False
      return contact_database

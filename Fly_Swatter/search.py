import numpy as np
import scipy
import time
import sched
import random

def target_check(image):
  # test function to return true or false if a image
  # is recognized 
  # to simulate, roll die with 1/10 probability
  if random.randint(1,10) > 9:
    return True
  else:
    return False
  
def search_mode():
  # this needs to create a scheduled series of events and a quick break once a target is identified 
  # should schedule a scan and recoding of event, maybe implement a saving of initial target location
  scheduler = sched.scheduler(time.time, time.sleep)
  image = 'j' # need to make this sometime of radar/image recongition input
  search = True
  rotation_count = 0 
  
  target_mode = False
  while search:
    rotation_count = rotation_count + 1
    scheduler.enter(1,1, print, ("SCANNING"))
    scheduler.run()

    if target_check("image"):
      search = False
      print("TARGET SPOTTED")
      return True
    else:
      if rotation_count >= 10:
        search = False
        return False
      #rotate(phi, theta)

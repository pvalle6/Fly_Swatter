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

def capture_image():
  return image
  
def search_mode():
  # this needs to create a scheduled series of events and a quick break once a target is identified 
  # should schedule a scan and recoding of event, maybe implement a saving of initial target location
  scheduler = sched.scheduler(time.time, time.sleep)
  image = 'j'
  search = True
  target_spotted = False

  target_mode = False
  while search:
    scheduler.enter(1,1, print, ("SCANNING"))
    scheduler.run()

    if target_check("image"):
      search = False
      print("TARGET SPOTTED")
      target_mode = True
    else:
      #rotate(phi, theta)

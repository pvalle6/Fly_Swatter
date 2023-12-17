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

def rotate(phi_omega, theta_omega):
  # This function should call Ras Pi functions to rotate the camera or Weapon
  
  # insert raspi function for rotation in phi and theta directions
  return None

def capture_image():
  return image
  
def search_mode():
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

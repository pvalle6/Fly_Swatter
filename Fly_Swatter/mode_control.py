from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import search
from Fly_Swatter.Fly_Swatter import fire_mode
from Fly_Swatter.Fly_Swatter import target
from Fly_Swatter.Fly_Swatter import graph_trajectory

import numpy as np
import scipy
import time
import sched
import random

# this should be the master script of the comptuer that controls the interface between the two modes 
def system_run(search_runs = 1, seed_search = 0, seed_fire = 0, verbose = False, graphical = False):
  target_mode = search.search_mode(runs = search_runs, seed = seed_search)
  if target_mode:
    log = fire_mode.track_lock(seed = seed_fire)
    if verbose:
      print(log)

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
def system_run(search_runs = 1, seed_search = None, seed_fire = None, verbose = False, graphical = False, realism = 0):
  """ This is the main function for running the program. It starts both search_mode and if applicable fire_mode
      search_runs: default = 1, indicates how many times search_mode can run for if nothing is found
      seed_search: default = None, provides a seed for the calculation of the probablility of search finding something in a simulation; 10 returns True Everytime
      seed_fire: default = None, provides a seed for calculating random target coordinates; this may change if a solution is able to be found or not
      verbose: default = false, determines if a log is printed out by default or not 
      graphical: default = false, provides for if a graph should be printed or not
      realism: default = 0, 0 provides for laser projectile, gravityless, no air resistance; 1 provides for gravity based projectile
  """
  fire_on, first_loc = search.search_mode(runs = search_runs, seed = seed_search)
  if fire_on:
    log = fire_mode.track_lock(seed = seed_fire, realism = realism, first_loc = first_loc)
    solution, deltaXYZ, xyzTwo, missile_speed = log
    if verbose:
      print_log(solution)
    if graphical:
      if realism == 0:
        graph_trajectory.graph_solution(missile_speed, solution[1], solution[2], deltaXYZ, xyzTwo, solution[0])
      if realism == 1:
        graph_trajectory.plot_ballistic_trajectory(missile_speed, solution[1], solution[2], deltaXYZ, xyzTwo, solution[0])
def print_log(solution):
  # prints out the target solution
  print( "FIRING SOLUTION RESULTS: \n" + f"REAL TIME: {time.time()} \n" + f"Time to Target: {solution[0]}\nPhi to Target: {solution[1]}\nTheta to Target: {solution[2]}")

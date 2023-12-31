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

class system_run_args():
  def __init__(self, search_runs: int = 1, seed_search: int = None, seed_fire: int = None, verbose: bool = False, graphical: bool = False, realism: int = 0, engage: bool = True):
    self.search_runs = search_runs
    self.seed_search = seed_search
    self.seed_fire = seed_fire
    self.verbose = verbose
    self.graphical = graphical
    self.realism = realism
    self.engage = engage
    

# this should be the master script of the comptuer that controls the interface between the two modes 
def system_run(args):
  """ This is the main function for running the program. It starts both search_mode and if applicable fire_mode
      search_runs: default = 1, indicates how many times search_mode can run for if nothing is found
      seed_search: default = None, provides a seed for the calculation of the probablility of search finding something in a simulation; 10 returns True Everytime
      seed_fire: default = None, provides a seed for calculating random target coordinates; this may change if a solution is able to be found or not
      verbose: default = false, determines if a log is printed out by default or not 
      graphical: default = false, provides for if a graph should be printed or not
      realism: default = 0, 0 provides for laser projectile, gravityless, no air resistance; 1 provides for gravity based projectile
  """
  p_list = []
  contact_list = []
  id = 1
  fire_on, target_list = search.search_mode(runs = args.search_runs, seed_fire = args.seed_fire, seed_search = args.seed_search)
  for i in target_list:
    # going to want to move this into the search mode module
    contact_list.append(radar.contact(str(id), last_time = time.time(), last_loc = i, status = "unknown"))
    id = id + 1
  main_db = radar.contact_database(name = "main", contacts = contact_list)
  if args.graphical and fire_on:
    for i in target_list:
      x, y, z = target.calculate_ballistics_missile(i.r, i.phi, i.theta)
      p_list.append([x,y,z])
    graph_trajectory.plot_radar(p_list)
  if args.engage and fire_on:
    log = fire_mode.track_lock(seed = args.seed_fire, realism = args.realism, first_loc = target_list[0])
    solution, deltaXYZ, xyzTwo, missile_speed = log
    if check_null(solution, [None, None, None]) == False:
      if args.verbose:
        print_log(solution)
      if args.graphical:
        if args.realism == 0:
          graph_trajectory.graph_solution(missile_speed, solution[1], solution[2], deltaXYZ, xyzTwo, solution[0])
        if realism == 1:
          graph_trajectory.plot_ballistic_trajectory(missile_speed, solution[1], solution[2], deltaXYZ, xyzTwo, solution[0])
    else:
      print("Solution Not Found")
        
def print_log(solution):
  # prints out the target solution
  print( "FIRING SOLUTION RESULTS: \n" + f"REAL TIME: {time.time()} \n" + f"Time to Target: {solution[0]}\nPhi to Target: {solution[1]}\nTheta to Target: {solution[2]}")

def check_null(list_one,list_two):
  flag = True
  if len(list_one) == len(list_two):
    for i in range(len(list_one)):
      if list_one[i] != list_two[i]:
        flag = False
  else:
    flag = False
  return flag
    
  

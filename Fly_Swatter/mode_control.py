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

def system_run(args, db = None, t_num: int = 0):

  fire_on = False
  main_db = db 
  if db == None:
    # checks if there is a provided radar database
    p_list = [] # p_list holds the plotting details of contacts
    contact_list = [] # holds the list of contacts to be provided for the creation of a main_db
    id = 1 # sets the first id in the databse to 1 
    fire_on, target_list = search.search_mode(runs = args.search_runs, seed_fire = args.seed_fire, seed_search = args.seed_search) # simulates the finding of radar contacts
    for i in target_list: # iterates through said radar contacts
      # might wanna refactor this
      contact_list.append(radar.contact(str(id), last_time = time.time(), last_loc = i, status = "unknown")) # appends contact_list with strings and labeled radar contacts in order seen
      id = id + 1 # iterates IDs
    main_db = radar.contact_database(name = "main", contacts = contact_list) # creates a radar database from given contacts
  if args.graphical and fire_on: # checks if the graphical option and if any radar contacts were found
    for i in target_list: # iterates through targets to find the plots for different contacts
      x, y, z = target.calculate_ballistics_missile(i.r, i.phi, i.theta) # converts sphr  -> cart
      p_list.append([x,y,z]) # adds to the plot list targets for the radar
    graph_trajectory.plot_radar(p_list) # graphs the radar display
  if args.engage and fire_on: # checks if engage is enable and contacts were found
    log = fire_mode.track_lock(seed = args.seed_fire, realism = args.realism, first_loc = target_list[0]) # creates a log item for track lock engage
    solution, deltaXYZ, xyzTwo, missile_speed = log # returns graphical solutions for engagements
    # need to refactor as to be be able to choose targets and solution
    if check_null(solution, [None, None, None]) == False:
      if args.verbose:
        print_log(solution)
        if args.graphical:
          if args.realism == 0:
            graph_trajectory.graph_solution(missile_speed, solution[1], solution[2], deltaXYZ, xyzTwo, solution[0])
          if args.realism == 1:
            graph_trajectory.plot_ballistic_trajectory(missile_speed, solution[1], solution[2], deltaXYZ, xyzTwo, solution[0])

    else:
      print("Solution Not Found")
    
  return main_db       
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
    
  

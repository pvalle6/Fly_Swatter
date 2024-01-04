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

class db_gen_args():
  def __init__(self, search_runs: int = 1, seed_search: int = None, seed_fire: int = None):
    self.search_runs = search_runs
    self.s_seed = seed_search
    self.f_seed = seed_fire
 

def search_radar_db_gen(args):
    fire_on = False
    # assumes that a new DB must be created using the given arguments

    # holds the list of contacts provided by DB or to be created; 
    contact_list = []
    id = 1
    fire_on, target_list = search.search_mode(runs = args.search_runs, seed_fire = args.seed_fire,
                                               seed_search = args.seed_search)
    for i in target_list:
        contact_list.append(radar.contact(str(id), last_time = time.time(), last_loc = i, status = "unknown"))
      id = id + 1 # iterates IDs
    main_db = radar.contact_database(name = "main", contacts = contact_list)
    return main_db

def choose_target(target_id, main_db):
    return main_db.contacts[target_id]

def plot_radar_display(main_db):
    # need to grab the list of contacts in a database and return a list in the format of the target_list
    plot_list = []
    coord_list = []
    for contact in main_db.contacts:
        plot_list.append(contact.last_loc)
    for plot in plot_list:
        x, y, z in target.calculate_ballistics_missile(plot.r, plot.phi, plot.theta)
        coord_list.append([x,y,z])
    graph_trajectory.plot_radar(coord_list)
        
def engage_target(contact, f_seed, realism):
    return fire_mode.track_loc(seed = f_seed, realism = realism, first_loc = contact.last_loc)

def print_graph(solution, realism):
    sol, deltaXYZ, xyz_two, missile_speed = log
    if realism == 0:
        graph_trajectory.graph_solution(missile_speed, sol[1], sol[2], deltaXYZ, xyz_two, sol[0])
    if realism == 1:
        graph_trajectory.plot_ballistic_trajectory(missile_speed, sol[1], sol[2], deltaXYZ, xyz_two, sol[0])
    

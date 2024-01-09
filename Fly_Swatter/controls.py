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
  
    contact_database = search.search_mode(runs = args.search_runs, seed_fire = args.f_seed,
                                               seed_search = args.s_seed)
    print(contact_database.contacts)
    return contact_database

def choose_target(target_id, main_db):
    return main_db.contacts[target_id]

def plot_radar_display(main_db, tkbool, self_, self_root):
    # need to grab the list of contacts in a database and return a list in the format of the target_list
    plot_list = []
    coord_list = []
    for contact in main_db.contacts:
        plot_list.append(contact.last_loc)
    for plot in plot_list:
        x, y, z = target.calculate_ballistics_missile(plot.r, plot.phi, plot.theta)
        coord_list.append([x,y,z])
    graph_trajectory.plot_radar(coord_list, tkbool, self_, self_root)
        
def engage_target(contact, proj_type):
    return fire_mode.track_lock(contact, proj_type, "straight")

def print_graph(solution, realism):
    sol, deltaXYZ, xyz_two, missile_speed = log
    if realism == 0:
        graph_trajectory.graph_solution(missile_speed, sol[1], sol[2], deltaXYZ, xyz_two, sol[0])
    if realism == 1:
        graph_trajectory.plot_ballistic_trajectory(missile_speed, sol[1], sol[2], deltaXYZ, xyz_two, sol[0])
    

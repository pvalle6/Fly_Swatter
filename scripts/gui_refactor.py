import tkinter as tk
from tkinter import *
from tkinter import ttk

import time

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure

from Fly_Swatter.Fly_Swatter import mode_control, fire_mode, search, radar, target, graph_trajectory, controls

class GUI_App:
    def __init__(self):

        # creates the base window
        self.root = tk.Tk()
        self.root.wm_title("Fire Control")
        #self.canvas = FigureCanvasTkAgg(master=self.root)
        #self.canvas.draw() # trying to get this to work

        # creates 4 frames to organize the two windows
        self.frame = tk.Frame(self.root, relief = tk.GROOVE, borderwidth = 5)

        self.rd = tk.Frame(self.frame, relief = tk.GROOVE, borderwidth = 5)
        self.quadtop = tk.Frame(self.frame, relief = tk.RAISED, borderwidth = 5)
        self.quadright = tk.Frame(self.frame)

        ### grid
        self.real_bint = tk.IntVar(value = 0)

        self.verb_bool = False
        self.graph_bool = False
        self.engage_bool = False

        # creates a total target class and controller 
        self.totaltar = 0
        self.target_select = tk.IntVar(value = 0)

        # creates empty seed and fire seed variables 
        self.se_seed = None
        self.fi_seed = None
        self.se_runs = tk.IntVar(value = 10)

        # creates the header for the main window

        # packing seperately solves issues o# NoneType because the
        # generation of the new object is seperate and not of packed

        self.debug = tk.Button(self.quadtop, text = "Debug", command = self.debug)
        self.debug.grid(row = 0, column = 0)
        
        self.gen_button = tk.Button(self.quadtop, text = 'Generate DB', command = self.gen_db)
        self.gen_button.grid(row = 0, column = 1)

        self.manage_db_button = tk.Button(self.quadtop, text = "Manage Contacts", command = self.manage_ct_wd)
        self.manage_db_button.grid(row = 0, column = 2)

        self.exit_button = tk.Button(self.quadtop, text = "EXIT", command = self.destroy_loop)
        self.exit_button.grid(row = 0, column = 3)
        
        #####################
        
        self.target_controls = tk.Frame(self.quadright, relief = tk.GROOVE, borderwidth = 5)

        self.tar_con_butt = tk.Frame(self.target_controls, relief = tk.RAISED, borderwidth = 5)
        self.tar_con_butt.grid(row = 0, column = 0)
        
        self.tar_label = tk.Label(self.tar_con_butt, text = f"Total Targets: {self.totaltar}")
        self.tar_label.grid(row = 0, column = 0)
        self.tar_spin = tk.Spinbox(self.tar_con_butt,  textvariable = self.target_select, from_ = 0, to = self.totaltar)
        self.tar_spin.grid(row = 1, column = 0)
        
        self.engage_button = tk.Button(self.tar_con_butt, text = "Engage Target", command = self.engage_t)
        self.engage_button.grid(row = 2, column = 0)

        self.display_target = tk.Button(self.tar_con_butt, text = "Display Target Info", command = self.update_var_labels)
        self.display_target.grid(row = 3, column = 0)

        self.weapon_select = tk.IntVar()

        self.weapon_select_frame = tk.Frame(self.tar_con_butt, relief = tk.RAISED, borderwidth = 5)
        self.weapon_select_frame.grid(row = 4, column = 0)

        ###################


        self.miss_select_label = tk.Label(self.weapon_select_frame, text = "Weapon Select")
        self.missile_one = tk.Radiobutton(self.weapon_select_frame, text = "Laser", value = 0, variable = self.weapon_select)
        self.missile_two = tk.Radiobutton(self.weapon_select_frame, text = "Flak", value = 1, variable = self.weapon_select)
        self.missile_three = tk.Radiobutton(self.weapon_select_frame, text = "Missile", value = 2, variable = self.weapon_select)
        
        self.miss_select_label.grid(row = 2, column = 0)
        self.missile_one.grid(row = 3, column = 0)
        self.missile_two.grid(row = 4, column = 0)
        self.missile_three.grid(row = 5, column = 0)

        self.target_controls.grid(row = 2, column = 1)
        self.frame.pack()
        
        ###################

        self.target_info_frame = tk.Frame(self.target_controls, relief = tk.GROOVE, borderwidth = 5)
        self.ti_header = tk.Label(self.target_info_frame, text = "Target #")

        self.target_info_frame.grid(row = 4, column = 0, padx = 5, pady= 20)
        self.ti_header.grid(row = 1, column = 0, padx = 50)

        self.report_frame = tk.Frame(self.target_info_frame, relief = tk.GROOVE, borderwidth = 5)
        self.report_frame.grid(row = 2, column = 0)

        self.target_report_name = tk.Label(self.report_frame, text = f"NAME:")
        self.target_report_azimuth = tk.Label(self.report_frame, text = f"AZIMUTH:")
        self.target_report_distance = tk.Label(self.report_frame, text = f"DISTANCE:")
        self.target_report_speed = tk.Label(self.report_frame, text = f"SPEED:")
        
        self.target_report_name.grid(row = 0, column = 0, pady =10)
        self.target_report_azimuth.grid(row = 1, column = 0, pady =10)
        self.target_report_distance.grid(row = 2, column = 0, pady =10)
        self.target_report_speed.grid(row = 3, column = 0, pady =10)

        ####################
        
        self.quadtop.grid(row = 0, column = 0, columnspan = 2)

        self.rd.grid(row = 1, column = 0)

        self.quadright.grid(row = 1, column = 1)

        self.empty_db = radar.contact_database("empty", [])
        controls.plot_radar_display(self.empty_db, True, self, self.rd)

        # DEBUG MENU STUFF
        self.debug_window = tk.Tk()
        self.debug_window.withdraw()
        self.debug_l = tk.Label(self.debug_window, text = "Debug Window").pack()

        self.realism_button = tk.Checkbutton(self.debug_window, text='Realism', variable = self.real_bint).pack()

        self.new_args_button = tk.Button(self.debug_window, text = "New Args", command = self.debug_args).pack(side = BOTTOM)
        
        self.debug_se_label = tk.Label(self.debug_window, text = "Search Seed").pack()        
        self.se_seed_e = tk.Entry(self.debug_window, textvariable = self.se_seed)
        self.se_seed_e.pack()

        self.debug_fire_label = tk.Label(self.debug_window, text = "Fire Seed").pack()
        self.fire_seed_e = tk.Entry(self.debug_window, textvariable = self.fi_seed)
        self.fire_seed_e.pack()

        self.debug_runs_label = tk.Label(self.debug_window, text = "Number of Runs").pack()
        self.runs_e = tk.Entry(self.debug_window, textvariable = self.se_runs)
        self.runs_e.pack()

        ######

        self.r_name = "NA"
        self.r_azi = "NA"
        self.r_dist = "NA"
        self.r_speed = "NA"
        
        self.target_report_name_two = tk.Label(self.report_frame, text = self.r_name)
        self.target_report_azimuth_two = tk.Label(self.report_frame, text = self.r_azi)
        self.target_report_distance_two = tk.Label(self.report_frame, text = self.r_dist)
        self.target_report_speed_two = tk.Label(self.report_frame, text = self.r_speed)
        
        self.target_report_name_two.grid(row = 0, column = 1, pady =10)
        self.target_report_azimuth_two.grid(row = 1, column = 1, pady =10)
        self.target_report_distance_two.grid(row = 2, column = 1, pady =10)
        self.target_report_speed_two.grid(row = 3, column = 1, pady =10)

        # ENGAGE INFO FRAME

        self.engage_info_frame = tk.Frame(self.target_controls, relief = tk.GROOVE, borderwidth = 5)
        self.engage_header = tk.Label(self.engage_info_frame, text = "FIRING SOLUTION")

        self.engage_info_frame.grid(row = 5, column = 0, padx = 5, pady= 20)
        self.engage_header.grid(row = 1, column = 0, padx = 50)

        self.engage_report_frame = tk.Frame(self.engage_info_frame, relief = tk.GROOVE, borderwidth = 5)
        self.engage_report_frame.grid(row = 2, column = 0)

        self.phi_var = 0
        self.theta_var = 0
        self.time_var = 0

        self.phi_sol = tk.Label(self.engage_report_frame, text = f"Phi: {self.phi_var}")
        self.phi_sol.grid(row = 0, column = 0)
        self.theta_sol = tk.Label(self.engage_report_frame, text = f"Theta: {self.theta_var}")
        self.theta_sol.grid(row = 1, column = 0)
        self.time_sol = tk.Label(self.engage_report_frame, text = f"Time: {self.time_var}")
        self.time_sol.grid(row = 2, column = 0)

        ##################################

        # Manage Contact Database Window
        
        self.manager_ct = tk.Tk()
        self.manager_ct.withdraw()
        self.manager_frame = tk.Frame(self.manager_ct, relief = tk.GROOVE, borderwidth = 5)
        self.manager_frame.grid(row = 0, column = 0)
        
        self.man_label = tk.Label(self.manager_frame, text = "Contact Manager")
        self.man_label.grid(row = 0, column = 0)
        
        self.ct_remove = tk.Button(self.manager_frame, text = "Remove Contact")
        self.ct_remove.grid(row = 1, column = 0)
        
        self.ct_add = tk.Button(self.manager_frame, text = "Add Contact")
        self.ct_add.grid(row = 2, column = 0)

        self.ct_name_l = tk.Label(self.manager_frame, text = "Name")
        self.ct_name_e = tk.Entry(self.manager_frame)

        self.ct_phi_l = tk.Label(self.manager_frame, text = "Phi")
        self.ct_phi_e = tk.Entry(self.manager_frame)
        self.ct_theta_l = tk.Label(self.manager_frame, text = "Theta")
        self.ct_theta_e = tk.Entry(self.manager_frame)
        self.ct_rho_l = tk.Label(self.manager_frame, text = "Rho")
        self.ct_rho_e = tk.Entry(self.manager_frame)

        
        self.ct_name_l.grid(row = 3, column = 0)
        self.ct_name_e.grid(row = 4, column = 0)
        self.ct_phi_l.grid(row = 5, column = 0)
        self.ct_phi_e.grid(row = 6, column = 0) 
        self.ct_theta_l.grid(row = 7, column = 0) 
        self.ct_theta_e.grid(row = 8, column = 0)
        self.ct_rho_l.grid(row = 9, column = 0)
        self.ct_rho_e.grid(row = 10, column = 0)
        
        ## going to make a self.ct_last_loc object for this 
        
    def debug(self):
        self.debug_window.deiconify()
        
    def gen_db(self):
        self.main_args = controls.db_gen_args(3,None,None)
        self.main_db = controls.search_radar_db_gen(self.main_args)
        print("------------------")
        print("DATABASE GENERATED")
        print("CONTACTS:")
        self.totaltar = len(self.main_db.contacts)
        for contacts in self.main_db.contacts:
            print(contacts)
        self.plot_radar()
        self.update_var_labels()
        
    def update_var_labels(self):
        # label for number of contacts
        # NUMBER OF TARGETS LABEL
        self.tar_label.grid_forget()
        self.tar_label = tk.Label(self.tar_con_butt, text = f"Total Targets: {self.totaltar}")
        self.tar_label.grid(row = 0, column = 0)
        
        # TARGET SPINNER 
        self.tar_spin.grid_forget()
        self.tar_spin = tk.Spinbox(self.tar_con_butt,  textvariable = self.target_select, from_ = 0, to = self.totaltar)
        self.tar_spin.grid(row = 1, column = 0)


        self.target_report_name_two.grid_forget()
        self.target_report_azimuth_two.grid_forget()
        self.target_report_distance_two.grid_forget()
        self.target_report_speed_two.grid_forget()

        self.r_name = self.main_db.contacts[self.target_select.get()].name
        self.r_dist = self.main_db.contacts[self.target_select.get()].last_loc.r
        self.r_azi = self.main_db.contacts[self.target_select.get()].last_loc.theta
        
        self.target_report_name_two = tk.Label(self.report_frame, text = self.r_name)
        self.target_report_azimuth_two = tk.Label(self.report_frame, text = self.r_azi)
        self.target_report_distance_two = tk.Label(self.report_frame, text = self.r_dist)
        self.target_report_speed_two = tk.Label(self.report_frame, text = self.r_speed)

        self.target_report_name_two.grid(row = 0, column = 1, pady =10)
        self.target_report_azimuth_two.grid(row = 1, column = 1, pady =10)
        self.target_report_distance_two.grid(row = 2, column = 1, pady =10)
        self.target_report_speed_two.grid(row = 3, column = 1, pady =10)

    def update_engage_info(self):
        self.phi_sol.grid_forget()
        self.theta_sol.grid_forget()
        self.time_sol.grid_forget()
        self.engage_report_frame.grid_forget()
        
        self.phi_sol = tk.Label(self.engage_report_frame, text = f"Phi: {self.phi_var}")
        self.phi_sol.grid(row = 0, column = 0)
        self.theta_sol = tk.Label(self.engage_report_frame, text = f"Theta: {self.theta_var}")
        self.theta_sol.grid(row = 1, column = 0)
        self.time_sol = tk.Label(self.engage_report_frame, text = f"Time: {self.time_var}")
        self.time_sol.grid(row = 2, column = 0)
        self.engage_report_frame.grid(row = 2, column = 0)
        print("")
        
    def debug_args(self):
        self.se_seed = self.se_seed_e.get()
        self.fi_seed = self.fire_seed_e.get()
        self.main_args = controls.db_gen_args(self.se_runs,self.se_seed,self.fi_seed)
        print("")
        
    def plot_radar(self):

        self.canvas.get_tk_widget().pack_forget()
        controls.plot_radar_display(self.main_db, True, self, self.rd)
        
    def engage_t(self):
        
        self.selected_contact = self.main_db.contacts[self.target_select.get()]
        
        self.solution_set = controls.engage_target(self.selected_contact, self.weapon_select.get())
        
        self.solution, self.deltaXYZ, self.xyz_two, self.miss_speed = self.solution_set

        self.phi_var = self.solution[0]
        self.theta_var = self.solution[1]
        self.time_var = self.solution[2]

        self.update_engage_info()
        print(f"Solutiom: {self.solution}")

    def manage_ct_wd(self):
        self.manager_ct.deiconify()

    def destroy_loop(self):
        self.root.destroy()
        
    def run(self):
        self.root.mainloop()
GUI_App().run()

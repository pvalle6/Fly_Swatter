import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib

import time

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


from Fly_Swatter.Fly_Swatter import mode_control, fire_mode, search, radar, target, graph_trajectory

class GUI_App:
    def __init__(self):


        # creates the base window
        self.root = tk.Tk()
        self.root.wm_title("Fire Control")
        self.canvas = FigureCanvasTkAgg(master=self.root)
        self.canvas.draw() # trying to get this to work

        # creates 4 frames to organize the two windows
        self.frame = tk.Frame(self.root, relief = tk.GROOVE, borderwidth = 5)
        self.beta = tk.Frame(self.root, relief = tk.GROOVE, borderwidth = 5)
        self.gamma  = tk.Frame(self.root, relief = tk.RAISED, borderwidth = 5)
        self.delta  = tk.Frame(self.root, relief = tk.GROOVE, borderwidth = 5)

        # this tkinter variables are used in the creation of the argument object
        # these tkinter objects hold int values that will represent booleans
        self.verb_bint = tk.IntVar(value = 0)
        self.graph_bint = tk.IntVar(value = 0)
        self.real_bint = tk.IntVar(value = 0)
        self.engage_bint = tk.IntVar(value = 0)

        self.verb_bool = False
        self.graph_bool = False
        # real var takes in a int value anyway
        self.engage_bool = False

        

        # creates a total target class and controller 
        self.totaltar = 0
        self.total_tar_text = tk.StringVar(value = "0")
        self.target_select = tk.IntVar(value = 0)

        # creates a empty main database and empty args_ holder variable as a child of the GUI class
        self.args_ = None
        self.db_ =  None


        # creates empty seed and fire seed variables 
        self.se_seed = None
        self.fi_seed = None
        self.se_runs = tk.IntVar(value = 10)

        
        # creates a tkinter button to open the debug window for use in simulations
        self.debug_button = tk.Button(self.root, text = "Debug", command = self.open_debug).pack()

        # creates the header for the main window
        self.radar_l = tk.Label(self.root, text='Radar').pack()

        # creates three buttons for use in the main display
        self.verbose_button = tk.Checkbutton(self.frame, text='Verbose', variable = self.verb_bint, onvalue = 1, offvalue = 0, command = self.check_button)
        self.graph_button = tk.Checkbutton(self.frame, text='Graphical', variable = self.graph_bint, command = self.check_button)
        self.engage_button = tk.Checkbutton(self.frame, text='Engage', variable = self.engage_bint, command = self.check_button)


        # packing seperately solves issues of NoneType because the generation of the new object is seperate and not of packed
        self.verbose_button.pack()
        self.graph_button.pack()
        self.engage_button.pack()
        
        #self.prev_db = tk.Checkbutton(self.root, text='DB_Loaded', variable = self.db_bool).pack()

        # updated to spinbox functionality instead of two buttons
        #self.increment_int = tk.Button(self.root, text = 'Next Target', command = self.next_t).pack()
        #self.decrement_int = tk.Button(self.root, text = 'Prev Target', command = self.prev_t).pack()
        self.run_button = tk.Button(self.gamma, text = 'Generate DB', command = self.sys)
        self.run_button.pack()
        
        self.frame.pack(side = TOP)
        self.delta.pack(side = TOP)
        self.beta.pack(side = LEFT)
        self.gamma.pack(side = RIGHT)
        
    # this is the function called for creating the debug window 
    def open_debug(self):
        self.debug_w = tk.Tk()
        self.debug_l = tk.Label(self.debug_w, text = "Debug Window").pack()
        self.realism_button = tk.Checkbutton(self.debug_w, text='Realism', variable = self.real_bint, command = self.check_button).pack()


        self.new_args_button = tk.Button(self.debug_w, text = "New Args", command = self.new_args).pack(side = BOTTOM)
        self.debug_se_label = tk.Label(self.debug_w, text = "Search Seed").pack()
        self.se_seed_e = tk.Entry(self.debug_w, textvariable = self.se_seed)
        self.se_seed_e.pack()
        self.debug_fire_label = tk.Label(self.debug_w, text = "Fire Seed").pack()
        self.fire_seed_e = tk.Entry(self.debug_w, textvariable = self.fi_seed)
        self.fire_seed_e.pack()
        self.debug_runs_label = tk.Label(self.debug_w, text = "Number of Runs").pack()
        self.runs_e = tk.Entry(self.debug_w, textvariable = self.se_runs)
        self.runs_e.pack()


        self.check_db_button = tk.Button(self.debug_w, text = "check db", command = self.check_db)
        self.check_db_button.pack()
    def check_db(self):
        print('')
        print(self.args_)
        print(self.db_)
    # function to creating a new database and providing it as a argument for the system run
    def new_args(self):
        self.db_ = None
        self.total_tar_text.set("Targets Avaliable: None")
        
        self.se_seed = int(self.se_seed_e.get())
        self.fi_seed = int(self.fire_seed_e.get())
        self.se_runs = int(self.runs_e.get())
        self.check_button()
        self.args_ = mode_control.system_run_args(search_runs = self.se_runs, seed_search = self.se_seed, seed_fire = self.fi_seed, verbose = self.verb_bool,
                                                      graphical = self.graph_bool, realism = self.real_bint, engage = self.engage_bool)

    # main function for running the program through the gui
    def sys(self):
        print("SYSTEM START")
        self.check_button()
        if self.args_ == None:
            self.args_ = mode_control.system_run_args(search_runs = 3, seed_search = None, seed_fire = None, verbose = self.verb_bool,
                                                      graphical = self.graph_bool, realism = 0, engage = self.engage_bool)

        else:
            print("ARGS  LOADED")
            print(time.time())
            mode_control.system_run(self.args_, self.db_, self.target_select.get())
        print(time.time())
        self.db_ = mode_control.system_run(self.args_)
            
        print("")
        print("New Radar ARGS Created and Loaded")
        self.check_button()
        self.totaltar = 0
        for i in self.db_.contacts:
            self.totaltar = self.totaltar + 1
                    
            print(i.name)
        self.total_tar_text.set("Targets Avaliable: " + str(self.totaltar))

        # creates the controller for target selection
        self.tar_label = tk.Label(self.beta, text = "Target #").pack()
        
        #self.tar_spin.pack()
        

        self.target_l = tk.Label(self.delta, textvariable = self.total_tar_text).pack()
        self.tar_spin = tk.Spinbox(self.beta,  textvariable = self.target_select, from_ = 0, to = self.totaltar, command = self.check_button)
        self.tar_spin.pack()
        print("")
    # starts the gui program

    def run(self):
        self.root.mainloop()
    # prints a display to console for checking to see if interface works (mostly used before implementing)
    def check_button(self):

        if self.engage_bint.get() == 0:
            self.engage_bool = False
        else:
            self.engage_bool = True
        if self.verb_bint.get() == 0:
            self.verb_bool = False
        else:
            self.verb_bool = True
        if self.graph_bint.get() == 0:
            self.graph_bool = False
        else:
            self.graph_bool = True
    
        print("-------------------")
        #print(f"Verbose: {self.verb_bool}")
        #print(f"Graphical: {self.graph_bool}")
        #print(f"Realism: {self.real_var.get()}")
        #print(f"Database: {self.db_bool}")                     
        #print(f"Engage: {self.engage_bool}")
        #print(f"Avaliable Targets #: {self.totaltar}")
        #print(f"Target Selected #: {self.target_select.get()}")
        print("-------------------")
GUI_App().run()

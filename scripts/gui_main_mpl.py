import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


from Fly_Swatter.Fly_Swatter import mode_control, fire_mode, search, radar, target, graph_trajectory

class GUI_App:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.wm_title("Fire Control")
        self.canvas = FigureCanvasTkAgg(master=self.root)
        self.canvas.draw()
        self.frame = tk.Frame(self.root, relief = tk.GROOVE, borderwidth = 5)
        self.beta = tk.Frame(self.root, relief = tk.GROOVE, borderwidth = 5)
        self.gamma  = tk.Frame(self.root, relief = tk.RAISED, borderwidth = 5)
        self.delta  = tk.Frame(self.root, relief = tk.GROOVE, borderwidth = 5)

        
        self.verb_bool = tk.BooleanVar()
        self.graph_bool = tk.BooleanVar()
        self.real_var = tk.IntVar(value = 0)
        self.engage_var = tk.BooleanVar()
        self.db_bool = tk.BooleanVar()

        self.totaltar = 0
        self.total_tar_text = tk.StringVar(value = "0")
        self.target_select = tk.IntVar(value = 0)

        self.args_ = None
        self.db_ =  None

        self.debug_button = tk.Button(self.root, text = "Debug", command = self.open_debug).pack()

        self.radar_l = tk.Label(self.root, text='Radar').pack()
        
        self.verbose_button = tk.Checkbutton(self.frame, text='Verbose', variable = self.verb_bool, command = self.check_button).pack()
        self.graph_button = tk.Checkbutton(self.frame, text='Graphical', variable = self.graph_bool, command = self.check_button).pack()
        self.engage_button = tk.Checkbutton(self.frame, text='Engage', variable = self.engage_var, command = self.check_button).pack()

        
        self.tar_label = tk.Label(self.beta, text = "Target #").pack()
        self.tar_spin = tk.Spinbox(self.beta,  textvariable = self.target_select, from_ = 0, to = 5, command = self.check_button).pack()

        self.target_l = tk.Label(self.delta, textvariable = self.total_tar_text).pack()

        
        #self.prev_db = tk.Checkbutton(self.root, text='DB_Loaded', variable = self.db_bool).pack()

        # updated to spinbox functionality instead of two buttons
        #self.increment_int = tk.Button(self.root, text = 'Next Target', command = self.next_t).pack()
        #self.decrement_int = tk.Button(self.root, text = 'Prev Target', command = self.prev_t).pack()
        self.run_button = tk.Button(self.gamma, text = 'run', command = self.sys).pack()
        
        self.frame.pack(side = TOP)
        self.delta.pack(side = TOP)
        self.beta.pack(side = LEFT)
        self.gamma.pack(side = RIGHT)
        
        
    def open_debug(self):
        self.debug_w = tk.Tk()
        self.debug_l = tk.Label(self.debug_w, text = "Debug Window").pack()
        self.realism_button = tk.Checkbutton(self.debug_w, text='Realism', variable = self.real_var, command = self.check_button).pack()


        self.new_db_button = tk.Button(self.debug_w, text = "New DB", command = self.delete_db).pack()
        self.debug_se_label = tk.Label(self.debug_w, text = "Search Seed").pack()
        self.se_seed_e = tk.Entry(self.debug_w).pack()
        self.debug_fire_label = tk.Label(self.debug_w, text = "Fire Seed").pack()
        self.fire_seed_e = tk.Entry(self.debug_w).pack()
        self.debug_runs_label = tk.Label(self.debug_w, text = "Number of Runs").pack()
        self.runs_e = tk.Entry(self.debug_w).pack()
          
    def delete_db(self):
        self.db_ = None
        self.total_tar_text.set("Targets Avaliable: None")
    def sys(self):
        print("SYSTEM START")
        
        if self.db_ == None:
            self.args_ = mode_control.system_run_args(search_runs = 5, seed_search = None, seed_fire = None, verbose = self.verb_bool.get(),
                                                      graphical = self.graph_bool.get(), realism = self.real_var.get(), engage = self.engage_var.get())
            self.db_ = mode_control.system_run(self.args_)
            self.db_bool = True
            print("")
            print("New Radar Database Created and Loaded")
            self.check_button()
            if self.db_ != None:
                for i in self.db_.contacts:
                    self.totaltar = self.totaltar + 1
                    
                    print(i.name)
                self.total_tar_text.set("Targets Avaliable: " + str(self.totaltar))
                print("")
        else:
            print("DATABASE LOADED")
            mode_control.system_run(self.args_, self.db_, self.target_select.get())
            
    def run(self):
        self.root.mainloop()
    def check_button(self):
        print("-------------------")
        #print(f"Verbose: {self.verb_bool.get()}")
        #print(f"Graphical: {self.graph_bool.get()}")
        #print(f"Realism: {self.real_var.get()}")
        print(f"Database: {self.db_bool}")                     
        #print(f"Engage: {self.engage_var.get()}")
        print(f"Avaliable Targets #: {self.totaltar}")
        print(f"Target Selected #: {self.target_select.get()}")
        print("-------------------")
GUI_App().run()

import tkinter as tk
from tkinter import ttk

from Fly_Swatter.Fly_Swatter import mode_control, fire_mode, search, radar, target, graph_trajectory

class GUI_App:
    def __init__(self):
        
        self.root = tk.Tk()
        self.verb_bool = tk.BooleanVar()
        self.graph_bool = tk.BooleanVar()
        self.real_var = tk.IntVar(value = 1)
        self.engage_var = tk.BooleanVar()
        self.db_bool = tk.BooleanVar()
        self.target_select = 0

        self.args_ = None
        self.db_ =  None

        
        self.verbose_button = tk.Checkbutton(self.root, text='Verbose', variable = self.verb_bool, command = self.check_button).pack()
        self.graph_button = tk.Checkbutton(self.root, text='Graphical', variable = self.graph_bool, command = self.check_button).pack()
        self.realism_button = tk.Checkbutton(self.root, text='Realism', variable = self.real_var, command = self.check_button).pack()
        self.engage_button = tk.Checkbutton(self.root, text='Engage', variable = self.engage_var, command = self.check_button).pack()
        self.prev_db = tk.Checkbutton(self.root, text='DB_Loaded', variable = self.db_bool).pack()
        
        self.increment_int = tk.Button(self.root, text = 'Next Target', command = self.next_t).pack()
        self.decrement_int = tk.Button(self.root, text = 'Prev Target', command = self.prev_t).pack()

        
        self.run_button = tk.Button(self.root, text = 'run', command = self.sys).pack()

    def sys(self):

        if self.db_ == None:
            self.args_ = mode_control.system_run_args(search_runs = 1, seed_search = None, seed_fire = None, verbose = self.verb_bool.get(),
                                                      graphical = self.graph_bool.get(), realism = self.real_var.get(), engage = self.engage_var.get())
            self.db_ = mode_control.system_run(self.args_)
            self.db_bool = True
            print("")
            print("New Radar Database Created and Loaded")
            for i in self.db_.list_contacts:
                print(i.name)
            print("")
        else:
            mode_control.system_run(self.args_, self.db_, self.target_select)
        
    def next_t(self):
        self.target_select = self.target_select + 1
        self.check_button()
    def prev_t(self):
        if self.target_select != 0:
            self.target_select = self.target_select - 1
        else:
            print("First Target Selected")
        self.check_button()

    def run(self):
        self.root.mainloop()
    def check_button(self):
        print("-------------------")
        print(f"V: {self.verb_bool.get()}")
        print(f"G: {self.graph_bool.get()}")
        print(f"R: {self.real_var.get()}")
        print(f"DB: {self.db_bool}")                     
        print(f"E: {self.engage_var.get()}")
        print(f"Tar: {self.target_select}")
        print("-------------------")
        
GUI_App().run()

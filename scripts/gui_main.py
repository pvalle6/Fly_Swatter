import tkinter as tk


from Fly_Swatter.Fly_Swatter import mode_control, fire_mode, search, radar, target, graph_trajectory

class GUI_App:
    def __init__(self):
        
        self.root = tk.Tk()
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar()
        self.var_2 = tk.IntVar(value = 1)
        self.var_3 = tk.BooleanVar()
        
        self.verbose_button = tk.Checkbutton(self.root, text='Verbose', variable = self.var_0, command = self.check_button).pack()
        self.graph_button = tk.Checkbutton(self.root, text='Graphical', variable = self.var_1, command = self.check_button).pack()
        self.realism_button = tk.Checkbutton(self.root, text='Realism', variable = self.var_2, command = self.check_button).pack()
        self.engage_button = tk.Checkbutton(self.root, text='Engage', variable = self.var_3, command = self.check_button).pack()
        
        self.run_button = tk.Button(self.root, text = 'run', command = self.sys).pack()

    def sys(self):
        mode_control.system_run(search_runs = 1, seed_search = None, seed_fire = None, verbose = self.var_0, graphical = self.var_1, realism = self.var_2.get(), engage = self.var_3)
        
    def run(self):
        self.root.mainloop()
    def check_button(self):
        print(f"V: {self.var_0.get()}")
        print(f"G: {self.var_1.get()}")
        print(f"R: {self.var_2.get()}")                                                                  
        print(f"E: {self.var_3.get()}")                                 
        
GUI_App().run()

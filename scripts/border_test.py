import tkinter as tk
from tkinter import *
from tkinter import ttk

import time

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure

from Fly_Swatter.Fly_Swatter import mode_control, fire_mode, search, radar, target, graph_trajectory, controls

from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure

def plot_radar(p_list, tkbool, self_, self_root):
  """ Creates a radar display like graph of a given target"""
  # (update to multiple contacts in future)
  #fig = plt.figure()
  #ax = plt.axes()

  fig, ax = plt.subplots()
  ax.set_facecolor('#131337')

  plt.tight_layout()
  ax.margins(x=0,y=0)
  #plt.grid(b = None)
  for i in [1.5, 3, 6, 10]:
    ring = plt.Circle((0,0),radius=i, color = "green", fill = False, linewidth = .3)
    ax.add_patch(ring)


  ax.set_xbound(-15,15)
  ax.set_ybound(-15,15)

  #ax.autoscale_view('tight')

  for i in [1.5, 3, 6]:
    ax.annotate(f"{i} m", (0.1, i + 0.01), color = "green", ha='center',fontsize=5)


  # this is just creating background 
  theta = np.pi / 2
  for i in range(0, 360, 10):
    ax.annotate(f"{i}", (np.cos(theta) * 10.6, np.sin(theta) * 10.6 - 0.3), color = "green", ha='center', fontsize=8)
    theta = theta - (np.pi * 2 / (360 / 10))
  plt.xticks([])
  plt.yticks([])
  

  for i in p_list:
    x, y, z = i 
    z = np.trunc(z * 1000) / 1000
    plt.scatter(x,y, s = 9, color = "red", marker='s')
    ax.annotate(f"UC {(z)} m", (x + 0.2, y), color = "red", ha = "left", fontsize = 3.5)
  # this is just creating the background

  plt.gca().set_axis_off()
  plt.gca().xaxis.set_major_locator(plt.NullLocator())
  plt.gca().xaxis.set_major_locator(plt.NullLocator())
  plt.gca().yaxis.set_major_locator(plt.NullLocator())
  if tkbool:
    self_.canvas = FigureCanvasTkAgg(fig, master=self_root)
    self_.canvas.draw()
    self_.canvas.get_tk_widget().grid(row =0, column = 0, pady=0,padx=0,)
  else:
    plt.show()
    
def plot_radar_display(main_db, tkbool, self_, self_root):
    # need to grab the list of contacts in a database and return a list in the format of the target_list
    plot_list = []
    coord_list = []
    for contact in main_db.contacts:
        plot_list.append(contact.last_loc)
    for plot in plot_list:
        x, y, z = target.calculate_ballistics_missile(plot.r, plot.phi, plot.theta)
        coord_list.append([x,y,z])
    plot_radar(coord_list, tkbool, self_, self_root)


class app:
    def __init__(self):
        self.display = tk.Tk()
        self.frame = tk.Frame(self.display, relief = tk.RAISED, borderwidth=2)
        
        self.empty_db = radar.contact_database("empty", [])
        plot_radar_display(self.empty_db, True, self, self.frame)
        self.frame.pack()
        #f, a  = plt.subplots()
       

        #plt.show()
        #self.canvas = FigureCanvasTkAgg(f, master=self.frame)
        
        #self.canvas.draw()
        #self.canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

    def run(self):
        self.display.mainloop()
app().run()

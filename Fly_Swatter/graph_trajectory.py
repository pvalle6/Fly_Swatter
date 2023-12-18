from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def graph_solution(missile_speed, phi, theta):

  x, y, z = target.calculate_ballistics_missile(missile_speed, phi, theta)
  fig = plt.figure()
  ax = plt.axes(projection='3d')

  ax.set_xlim(xmin=-.5, xmax=.5)a
  ax.set_ylim(ymin=-.5, ymax=.5)
  ax.set_zlim(zmin=0, zmax=2)

  xline = np.linspace(0,x,100)
  yline = np.linspace(0,y,100)
  zline = np.linspace(0,z,100)

  
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z');
 
  ax.plot3D(xline, yline, zline, 'red')

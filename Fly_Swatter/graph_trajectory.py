from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def plot_radar(p_list):
  """ Creates a radar display like graph of a given target"""
  # (update to multiple contacts in future)
  fig = plt.figure(dpi=200)
  ax = plt.axes()
  ax.set_facecolor('#131337')

  #plt.grid(b = None)
  for i in [1.5, 3, 6, 10]:
    ring = plt.Circle((0,0),radius=i, color = "green", fill = False, linewidth = .3)
    ax.add_patch(ring)

  ax.set_xbound(-12,12)
  ax.set_ybound(-12,12)

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
  
  
def graph_solution(missile_speed, phi, theta, deltaXYZ_target, xyz_target, time):
  """ Function that generates a graphical representation of the target's location 
      and velocity vector as well as the missile travel path and interception for a laser like solution
  """
  mx, my, mz = target.calculate_ballistics_missile(missile_speed * time, phi, theta)
  tx, ty, tz = xyz_target
  dtx, dty, dtz = deltaXYZ_target

  fig = plt.figure()
  ax = plt.axes(projection='3d')

  #ax.set_xlim(xmin=-2, xmax=2)
  #ax.set_ylim(ymin=-2, ymax=2)
  #ax.set_zlim(zmin=0, zmax=2)


  txline = np.linspace(tx,tx + dtx * time, 1000)
  tyline = np.linspace(ty,ty + dty * time, 1000)
  tzline = np.linspace(tz,tz + dtz * time, 1000)

  mxline = np.linspace(0,mx,100)
  myline = np.linspace(0,my,100)
  mzline = np.linspace(0,mz,100)


  ax.legend()

  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z');

  ax.plot3D(txline, tyline, tzline, 'grey', label='Target Trajectory')
  ax.plot3D(mxline, myline, mzline, 'red', label='Missile Trajectory')
  
  ax.legend()
  plt.show()

def plot_ballistic_trajectory(initial_missile_speed, phi, theta, deltaXYZ_target, xyz_target, time):
  """ Function that generates a graphical representation of the target's location 
      and velocity vector as well as the missile travel path and interception for a ballistic and parabolic like solution
  """
  mx, my, mz = target.calculate_ballistics_missile(initial_missile_speed, phi, theta)

  tx, ty, tz = xyz_target
  dtx, dty, dtz = deltaXYZ_target

  fig = plt.figure()
  ax = plt.axes(projection='3d')


  txline = np.linspace(tx,tx + dtx * time, 1000)
  tyline = np.linspace(ty,ty + dty * time, 1000)
  tzline = np.linspace(tz,tz + dtz * time, 1000)

  g = 9.81

  mxline = np.linspace(0,mx * time,100)
  myline = np.linspace(0,my * time ,100)
  z_parabola = -(g / 2) * ((myline / my) ** 2) + (mz * (myline / my))


  ax.legend()

  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z');

  ax.plot3D(txline, tyline, tzline, 'grey', label='Target Trajectory')
  ax.plot3D(mxline, myline, z_parabola, 'red', label='Missile Trajectory')

  ax.legend()
  plt.show()

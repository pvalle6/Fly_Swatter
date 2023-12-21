from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def graph_solution(missile_speed, phi, theta, deltaXYZ_target, xyz_target, time):
  # function that enables a quick 3d plot of the missile launch and interception of a straight-course target
  # probably need to update with a non-straight course target and non straight missile path
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
  # function that enables a quick 3d plot of the missile launch and interception of a straight-course target
  # probably need to update with a non-straight course target and non straight missile path
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

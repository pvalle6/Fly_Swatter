# import numpy as np
# import scipy
# import time
# import sched
# import random

# from Fly_Swatter.Fly_Swatter import radar
# from Fly_Swatter.Fly_Swatter import target

# class ballistic():
#   def __init__(self, name, btype, status, thetai, phii, xi, yi, zi, speedi):
#     # initiallization should be considered the initial position and velocity of the object
#     # again it should be noted that theta and phi are not in refernece to the origin but to the angle at which the object is continuing
#     self.name = name
#     self.btype = btype
#     self.status = status
#     self.thetai = thetai
#     self.phii = phii
#     self.xi = xi
#     self.yi = yi
#     self.zi = zi
#     self.speed = speedi
#     self.life_time = time.time() # relatively zero, absolutely to unix
    
#   def get_loc_speed(time_sample):
#     if self.btype == "simple_kin":
#       # this option should use the kinematic equations and unix time to calculate the trajectory and return locations and velocity vectors
#       gravity = 9.81
#       # this is the correct function for conversion between each as it uses its own origin as reference for phi and theta
#       deltaXYZ = target.calculate_ballistics_missile(self.speed, self.phi, self.theta):
#       deltaT = time.time() - self.life_time # this can be substitued for controlled deltaT
#       dxi,dyi,dzi = deltaXYZ

#       # kinematic equations
#       xtwo = xi + (dxi) * deltaT #no gravity
#       ytwo = yi + (dyi) * deltaT #no gravity
#       ztwo = zi + (dzi) * deltaT - (0.5) * (gravity) * (deltaT ** 2) 

#       # need to check for negative value when taking the square root
#       # x and y steps can be skipped for computational simplicity 
#       #dxtwo_square = (dxi ** 2) 
#       dxtwo = dxi
#       #dytwo_square = (dyi ** 2) 
#       dytwo = dyi

#       dyztwo_square = (dzi ** 2) - 2 * (gravity) (ztwo - zi)

#       #prevents irrational formation, idk if that would happen though
      
#       if dyztwo_square =< 0:
#         dyztwo = np.sqrt(-dyztwo_square)
#       else:
#         dyztwo = np.sqrt(dyztwo_square)
  
#       xyz_two = [xtwo, ytwo, ztwo] 
#       dxyz_two = [dxtwo, dytwo, dztwo]
#       return [xyz_two, dxyz_two]
#     else:
#       # Runge Kutta Hell
#       # I haven't put air resistance
#       # I also could merge and implement straight line kinematics in here or continuous flights

    


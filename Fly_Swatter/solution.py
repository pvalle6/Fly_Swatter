from Fly_Swatter.Fly_Swatter import radar
#from Fly_Swatter.Fly_Swatter import search
from Fly_Swatter.Fly_Swatter import target


# need to create a better system for identifying target trajectory, probably more differential equations
# as it currently exists, it is mostly a taylor series approximation 

deltaT, deltaXYZ, xyz_one, xyz_two = calculate_trajectory_target(first_loc, second_loc)

guess_solution = xyz_two
guess_solution = xyz_two # need to replace this time factor with a better estimation

solution = scipy.optimize.fsolve(find_firing_solution, guess_solution, args=(deltaXYZ, xyz_two, missile_speed))

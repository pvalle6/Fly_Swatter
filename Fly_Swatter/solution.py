from Fly_Swatter.Fly_Swatter import radar
#from Fly_Swatter.Fly_Swatter import search
from Fly_Swatter.Fly_Swatter import target
# probably going to have to create a differential equation solver for this one
deltaT, deltaXYZ, xyz_one, xyz_two = calculate_trajectory_target(first_loc, second_loc)

guess_solution = xyz_two
solution = xyz_two # need to replace this time factor with a better estimation

solution = scipy.optimize.fsolve(find_firing_solution, guess_solution, args=(deltaXYZ, xyz_two, missile_speed))

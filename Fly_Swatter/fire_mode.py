from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target

# might want to have this part coded before the switch to improve computational effiency and not delay time to solution
def check_valdity(solution):
  if solution[0] <= 0.05:
    return False
  else:
    return True
    
def laser_handler(first_loc):
  deltaT, deltaXYZ, xyz_one, xyz_two = radar.calculate_trajectory_target(first_loc)
  guess_solution = xyz_two
  solution = scipy.optimize.fsolve(target.laser_solution, guess_solution, args=(deltaXYZ, xyz_two, missile_speed))
  if(check_valdity(solution)):
    return [solution, True]
  else:
    return [None, False]
  
def track_lock(realism, projectile_type, target_course):
  # three realism levels to calculate for 
  if realism == 0 and projectile_type == "bullet" and target_course == "straight":
    # this case is basically a single fire laser
    validity = False
    #only part actually coded for
    print("SOLUTION INCOMING")
    first_loc = radar.generate_random_vector(2, 2) # this needs to substituted for the same sim as the search mode

    solution, validity = laser_handler(first_loc)
    if validity:
      print("Solution Found")
      print(f"Time to Target: {solution[0]}")
      print(f"Phi to Target: {solution[1]}")
      print(f"Theta to Target: {solution[2]}")
    else:
      print("NO SOLUTION YET AVALIABLE, INVALID AZMIMUTH")
  else:
      print("NO SOLUTION YET AVALIABLE, OUT OF BOUNDS")
    
  
  # should activate when first detect a target from search mode 

  # should schedule a check to see if a firing solution is avaliable
  # if none is avalaible, two options, calculate a likely probably solution or
  # wait and check for another solution if avaliable


  # might want to create a return to search mode 

  # need to slave RADAR and launcher together when target mode is activated

  # once firing solution is calculated, fire, and reset

class azimuth_control():
  # class for controlling the orientation of the launch system and radar
  # need to implement controls for slaving launch system to radar
  def __init__(self, name, status, theta, phi, x, y, z):
    self.name = name
    self.status = status
    self.theta = theta
    self.phi = phi
    self.x = x
    self.y = y
    self.z = z 

  def set_position(theta, phi, x, y, z):
    self.theta = theta
    self.phi = phi
    self.x = x
    self.y = y
    self.z = z

  def change_azimuth(d_theta, d_phi):
    self.theta = self.theta + d_theta
    self.phi = self.phi + d_phi

  def slave(controller):
    self.status = controller

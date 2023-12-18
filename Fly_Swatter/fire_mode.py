from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import target

# might want to have this part coded before the switch to improve computational effiency and not delay time to solution

def track_lock(realism, projectile_type):
  # three realism levels to calculate for 
  if realism == 0 and projectile_type = "straight":
    #only part actually coded for
    print("SOLUTION INCOMING")
  else:
    print("NO YET AVALIABLE")
    
  
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

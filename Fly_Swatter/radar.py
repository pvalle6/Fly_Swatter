# to calculate the ballistics of a target, two samples is the minimum required for a triangle to be created

# simple example assumes a sonar image (probably want to generalize this to radar or image recognition)
class target_loc():
  def __init__(self, phi, theta, r, time_spot):
    self.phi = phi
    self.theta = theta
    self.r = r
    self.time_spot = time_spot
  def tell(self):
    return (f"Phi: {self.phi}  " + f"Theta: {self.theta} " + f"Rho: {self.r}")

def target_radar_sight(return_data):
  # need a function that captures a location of the target
  time = time.time()
  return phi, theta, r, time

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

def generate_random_vector(max_distance):
  a = random.random() * (np.pi / 2)
  b = random.random() * (2 * np.pi)

  data_one = target_loc(a, b, random.random() * max_distance, 0)

  data_two = target_loc(a + 0.01, b + 0.01, 2 + 0.01, 0.2)

  return [data_one, data_two]

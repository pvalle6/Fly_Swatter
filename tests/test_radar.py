import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import mode_control
from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import search
from Fly_Swatter.Fly_Swatter import fire_mode
from Fly_Swatter.Fly_Swatter import target
from Fly_Swatter.Fly_Swatter import graph_trajectory

import unittest

class Test_Radar(unittest.TestCase):
  def test_vector_generation(self):
    self.assertEqual(radar.generate_random_vector(1).tell(), 'Phi: 0.15707963267948966  Theta: -0.3141592653589793 Rho: 1.1749139528992099')

  def test_calc_traj(self):
    self.assertEqual(radar.calculate_trajectory_target(radar.generate_random_vector(1), 1),[1,
 [0.13436424411240122, 0.8474337369372327, 0.7637746189766141],
 [0.30870158408348597, -0.10030322492702326, 2.0493683190167182],
 [0.4430658281958872, 0.7471305120102094, 2.8131429379933324]])
    
  def test_target_loc_class(self):
    self.assertEqual(radar.target_loc(0.24, 0.24, 2, time.time()).tell(), "Phi: 0.24  Theta: 0.24 Rho: 2")


if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)

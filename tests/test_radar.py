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
    self.assertEqual(radar.generate_random_vector(2,2,237).r, 2) # this must return the value of max_distance 

  def test_calc_traj(self):
    self.assertEqual(radar.calculate_trajectory_target(radar.generate_random_vector(2,2,237), 237),[1,
      [0.6225259266420455, 0.9050618497174403, 0.970205062907603],
      [1.2600735106701009, -1.2600735106701009, 0.9079809994790936],
        [1.8825994373121464, -0.35501166095266057, 1.8781860623866966]])
    
  def test_target_loc_class(self):
    self.assertEqual(radar.target_loc(0.24, 0.24, 2, time.time()).tell(), "Phi: 0.24  Theta: 0.24 Rho: 2")


if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)

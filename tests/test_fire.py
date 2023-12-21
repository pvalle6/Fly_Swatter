import unittest

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

class Test_Fire(unittest.TestCase):
  def test_validity(self):
    self.assertEqual(fire_mode.check_valdity([-1, 0.2, 0.3]), False)
  # def test_basic_fire(self):
  #   self.assertEqual(fire_mode.track_lock(seed = 1)[:23], "FIRING SOLUTION RESULTS")
if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)

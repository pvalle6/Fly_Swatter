import unittest

import numpy as np
import scipy
import time
import sched
import random


import radar
import search
import fire_mode
import target
import graph_trajectory

class Test_Fire(unittest.TestCase):
  def test_validity(self):
    self.assertEqual(fire_mode.check_valdity([-1, 0.2, 0.3]), False)
  def test_basic_fire(self):
    self.assertEqual(fire_mode.track_lock(seed = 1)[:23], "FIRING SOLUTION RESULTS")
if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)

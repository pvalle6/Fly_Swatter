import unittest

import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import radar
from Fly_Swatter.Fly_Swatter import search
from Fly_Swatter.Fly_Swatter import fire_mode
from Fly_Swatter.Fly_Swatter import target
from Fly_Swatter.Fly_Swatter import graph_trajectory

class Test_Fire(unittest.TestCase):
  def test_validity(self):
    self.assertEqual(fire_mode.check_valdity([-1, 0.2, 0.3]), False)

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)

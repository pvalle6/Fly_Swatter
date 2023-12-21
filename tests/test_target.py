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

class Test_target(unittest.TestCase):
  def test_conversion(self):
    self.assertEqual(target.calculate_ballistics_missile(10, 0.24,0.34), [2.240952600725227, 0.7927075768141941, 9.713379748520296])

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)

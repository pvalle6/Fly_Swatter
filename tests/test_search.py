import unittest

import numpy as np
import scipy
import time
import sched
import random

from Fly_Swatter.Fly_Swatter import search

class Test_Search(unittest.TestCase):
    def test_target_gen(self):
        txtout = "Phi: 0.1  Theta: 0.9424777960769379 Rho: 8.721937132416983"
        c, sloc = search.target_check(image = None, search_seed =10, fire_seed = 15)
        self.assertEqual(sloc.tell(), txtout)

                         
unittest.main()

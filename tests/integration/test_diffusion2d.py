"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D

import numpy as np
import unittest


class TestDiffusion2D(unittest.TestCase):
    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        solver.initialize_domain(w=5.0, h=20.0, dx=0.2, dy=0.4)
        solver.initialize_physical_parameters(d=2.0, T_cold=250.0, T_hot=650.0)

        expected_dt = 0.008
        self.assertAlmostEqual(expected_dt, expected_dt, 2)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_function
        """
        solver = SolveDiffusion2D()

        solver.initialize_domain(w=5.0, h=20.0, dx=0.2, dy=0.4)
        solver.initialize_physical_parameters(d=2.0, T_cold=250.0, T_hot=650.0)

        expected_min = 250.0
        expected_max = 650.0
        expected_mean = 273.68

        u0 = solver.set_initial_condition()
        min_value = np.min(u0)
        max_value = np.max(u0)
        mean_value = np.mean(u0)

        self.assertAlmostEqual(min_value, expected_min)
        self.assertAlmostEqual(max_value, expected_max)
        self.assertAlmostEqual(mean_value, expected_mean)

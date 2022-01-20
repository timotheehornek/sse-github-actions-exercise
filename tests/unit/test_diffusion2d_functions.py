"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
import unittest


class TestDiffusion2D(unittest.TestCase):
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        solver.initialize_domain(w=5.0, h=20.0, dx=0.2, dy=0.4)

        expected_nx = 25
        expected_ny = 50

        self.assertEqual(expected_nx, solver.nx)
        self.assertEqual(expected_ny, solver.ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()

        solver.w = 5.0
        solver.h = 20.0
        solver.dx = 0.2
        solver.dy = 0.4

        solver.nx = 25
        solver.ny = 50

        solver.initialize_physical_parameters(d=2.0, T_cold=250.0, T_hot=650.0)

        expected_dt = 0.008
        self.assertAlmostEqual(expected_dt, expected_dt)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_condition
        """
        solver = SolveDiffusion2D()

        solver.w = 5.0
        solver.h = 20.0
        solver.dx = 0.2
        solver.dy = 0.4

        solver.nx = 25
        solver.ny = 50

        solver.d = 2.0
        solver.T_cold = 250.0
        solver.T_hot = 650.0

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

        for indices in [[0, 0], [12, 11], [2, 3], [4, 33], [4, 33], [24, 49]]:
            self.assertAlmostEqual(u0[indices[0], indices[1]], expected_min)

        for indices in [[16, 14], [20, 9], [22, 15], [24, 17]]:
            self.assertAlmostEqual(u0[indices[0], indices[1]], expected_max)

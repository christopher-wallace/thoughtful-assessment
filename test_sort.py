#!/usr/bin/env python3

import unittest

from package_sorter import sort


class TestSortFunction(unittest.TestCase):
    def test_standard_package(self):
        """Not heavy and not bulky"""
        result = sort(width=10, height=10, length=10, mass=5)
        self.assertEqual(result, "STANDARD")

    def test_heavy_only(self):
        """Heavy but not bulky"""
        result = sort(width=10, height=10, length=10, mass=20)
        self.assertEqual(result, "SPECIAL")

    def test_bulky_only_by_dimension(self):
        """Bulky due to a large dimension but not heavy"""
        result = sort(width=150, height=10, length=10, mass=5)
        self.assertEqual(result, "SPECIAL")

    def test_bulky_only_by_volume(self):
        """Bulky due to volume but not heavy"""
        result = sort(width=100, height=100, length=100, mass=5)
        self.assertEqual(result, "SPECIAL")

    def test_heavy_and_bulky(self):
        """Both heavy and bulky"""
        result = sort(width=150, height=10, length=10, mass=20)
        self.assertEqual(result, "REJECTED")

    def test_boundary_mass(self):
        """Mass exactly at heavy threshold"""
        result = sort(width=10, height=10, length=10, mass=20)
        self.assertEqual(result, "SPECIAL")

    def test_boundary_dimension(self):
        """Dimension exactly at bulky threshold"""
        result = sort(width=149, height=149, length=150, mass=5)
        self.assertEqual(result, "SPECIAL")

    def test_boundary_volume(self):
        """Volume exactly at bulky threshold"""
        result = sort(width=100, height=100, length=100, mass=5)
        self.assertEqual(result, "SPECIAL")

if __name__ == "__main__":
    unittest.main()

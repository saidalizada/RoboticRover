import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from roboticrover import Robot, MoveRobot

class TestRoboticRover(unittest.TestCase):
    def test_move_or_spint(self):
        robot = Robot('E', 3, 4)
        robot.compute_move_or_spin('L')
        self.assertAlmostEqual(str(robot), '3 4 S')

    def test_move_robot(self):
        move_robot = MoveRobot()
        robot = Robot('E', 3, 4)
        move_robot.set_robot(robot)
        move_robot.compute(['L','L','M'])
        self.assertAlmostEqual(str(robot), '4 4 W')

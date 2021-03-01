""" robotic rover """
from .load_json import load_json
class Robot:
    """ Robot class, to compute each co-ordinates and cardinal compass points."""
    def __init__(self, compass_point, x, y):
        self.compass_point = compass_point
        self.x = x
        self.y = y
        self.left_spin = load_json('roboticrover/resources/turn_left.json')
        self.right_spin = load_json('roboticrover/resources/turn_right.json')

    def compute_move_or_spin(self, letter):
        if letter == 'L':
            self.compass_point = self.left_spin[self.compass_point]
        elif letter == 'R':
            self.compass_point = self.right_spin[self.compass_point]
        elif letter == 'M':
            if self.compass_point == 'N':
                self.y += 1
            elif self.compass_point == 'W':
                self.x += 1
            elif self.compass_point == 'S':
                self.y -= 1
            elif self.compass_point == 'E':
                self.x -= 1

    def __str__(self):
        return f"{self.x} {self.y} {self.compass_point}"

class MoveRobot:
    """ MoveRobot class, to move or spin robot for each letter (L, R, M) """
    def set_robot(self, robot):
        self.robot = robot

    def validate_letters(self, letters):
        for letter in letters:
            if letter not in ['L', 'R', 'M']:
                return False
        return True

    def compute(self, letters):
        for letter in letters:
            self.robot.compute_move_or_spin(letter)
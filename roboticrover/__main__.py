import sys
from .robotic_rover import Robot, MoveRobot

if __name__ == "__main__":

    try:
        input_file = sys.argv[1]
    except IndexError:
        print("Please add input file")
        exit(-1)

    f = open(input_file)
    Plateau = f.readline() 
    move_robot = MoveRobot()
    while True:
        line1 = f.readline()
        line2 = f.readline()
        if not line1 or not line2:
            break
        x, y, compass_point = line1.split()
        letters = list(line2.split())
        if move_robot.validate_letters(letters):
            robot = Robot(compass_point, int(x), int(y))
            move_robot.set_robot(robot)
            move_robot.compute(letters)
            print(robot)
        else:
            print(f"Check input file. The possible letters are 'L', 'R' and 'M'.")

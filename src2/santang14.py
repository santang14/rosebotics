"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
<<<<<<< HEAD:src/santang14.py
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    run_test_go_stop()


def run_test_go_stop():
    """ Tests the   go   and   stop   Snatch3rRobot methods. """
    robot = rb.Snatch3rRobot()

    robot.go(50, 25)
    time.sleep(2)
    robot.stop()

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())
    robot.left_wheel.reset_degrees_spun(0)

    time.sleep(2)

    robot.go(100, 100)
    time.sleep(3)
    robot.stop(rb.StopAction.COAST.value)

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())
=======
    """ Runs YOUR specific part of the project """
>>>>>>> aeca62ad3e504fadd0c49a8efdaddc9724011e05:src/m3.py


main()

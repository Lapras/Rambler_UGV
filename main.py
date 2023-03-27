#imports
import drivetrain
import time

DIR_FORWARD = 1
DIR_BACKWARD = -1
SIDE_RIGHT = False
SIDE_LEFT = True

#create drivetrain object
drivetrain = drivetrain.Drivetrain()

#test code or whatever here, for now
drivetrain.GPIOset()
drivetrain.setDirection(DIR_FORWARD, SIDE_RIGHT)
drivetrain.setDriection(DIR_FORWARD, SIDE_LEFT)

drivetrain.changeSpeed(30)
drivetrain.updateSpeed()

time.sleep(1)

drivetrain.changeSpeed(80)
drivetrain.updateSpeed()

time.sleep(1)

drivetrain.changeSpeed(0)
drivetrain.updateSpeed()
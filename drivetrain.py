import RPi.GPIO as GPIO

DIR_FORWARD = 1
DIR_BACKWARD = -1
SIDE_RIGHT = False
SIDE_LEFT = True

class Drivetrain:
    GPIO.setmode(GPIO.BOARD)

    #default constructor
    def __init__self():
        #TODO: Update pins for how we wire them
        EN1, IN1A, IN1B = 0,0,0
        EN2, IN2A, IN2B = 0,0,0
        EN3, IN3A, IN3B = 0,0,0
        EN4, IN4A, IN4B = 0,0,0

        speed = 0
    def GPIOset():
        #Setup motor one (Front Left)
        GPIO.setup(EN1, GPIO.OUT)
        GPIO.setup(IN1A, GPIO.OUT)
        GPIO.setup(IN2, GPIO.OUT)
        PWM1 = GPIO.PWN(EN1, 100)
        PWM1.start(0)

        #Setup motor two (Front Right)
        GPIO.setup(EN2, GPIO.OUT)
        GPIO.setup(IN2A, GPIO.OUT)
        GPIO.setup(IN2B, GPIO.OUT)
        PWM2 = GPIO.PWN(EN2, 100)
        PWM2.start(0)
        
        #Setup motor three (Back Right)
        GPIO.setup(EN3, GPIO.OUT)
        GPIO.setup(IN3A, GPIO.OUT)
        GPIO.setup(IN3B, GPIO.OUT)
        PWM3 = GPIO.PWN(EN3, 100)
        PWM3.start(0)

        #Setup motor four (Back left)
        GPIO.setup(EN4, GPIO.OUT)
        GPIO.setup(IN4A, GPIO.OUT)
        GPIO.setup(IN4B, GPIO.OUT)
        PWM4 = GPIO.PWN(EN4, 100)
        PWM4.start(0)
    
    #change the drive-wide speed variable that we will change our PWM duty cycles off of
    def changeSpeed(x):
        speed = x

    #set direction of motors given a side and direction argument
    #TODO: test motors and ensure they drive in the right direction given correct high/low arguments
    def setDirection(side, direction):
        if(side == SIDE_RIGHT):
            if(direction == DIR_FORWARD):
                GPIO.output(IN2A, GPIO.HIGH)
                GPIO.output(IN2B, GPIO.LOW)
                GPIO.output(IN3A, GPIO.HIGH)
                GPIO.output(IN3B, GPIO.LOW)
            elif(direction == DIR_BACKWARD):
                GPIO.output(IN2A, GPIO.LOW)
                GPIO.output(IN2B, GPIO.HIGH)
                GPIO.output(IN3A, GPIO.LOW)
                GPIO.output(IN3B, GPIO.HIGH)
        elif(side == SIDE_LEFT):
            GPIO.output(IN1A, GPIO.HIGH)
            GPIO.output(IN1B, GPIO.LOW)
            GPIO.output(IN4A, GPIO.HIGH)
            GPIO.output(IN4B, GPIO.HIGH)

    #Actually update the PWM speed, this will allow us to 'play' with out global speed variable
    #in the case that one of our motors is driving faster (which I've been told some of them are geared differently, so we will probably have to)
    def updateSpeed():
        PWM1.ChangeDutyCycle(speed)
        PWM2.ChangeDutyCycle(speed)
        PWM3.ChangeDutyCycle(speed)
        PWM4.ChangeDutyCycle(speed)
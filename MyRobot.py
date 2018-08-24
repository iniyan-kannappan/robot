import RPi.GPIO as GPIO
import time
import sys,tty,termios

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)
GPIO.setup([14, 15, 20, 21], GPIO.OUT)

def Forward():
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)

    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)

    time.sleep(0.5)
    Stop()



def Reverse():
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)

    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)

    time.sleep(0.5)
    Stop()

def Stop():
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)

    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

def Exit():
    Stop()
    exit()

def getch():

    fd=sys.stdin.fileno()
    old_settings=termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch=sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
    return ch

def Right():

    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)

    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)

    time.sleep(0.08)
    Stop()


def Left():
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)

    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)

    time.sleep(0.08)
    Stop()


while True:

    print('Enter a letter, F for Forward, B for Backward, R for Right,and L for Left, S for Stop, E for Exit.')
    letter=getch()

    if letter == "f":
        print('F')
        Forward()
    if letter == "b":
        print('B')
        Reverse()
    if letter == "r":
        print('R')
        Right()
    if letter == "l":
        print('L')
        Left()
    if letter == "s":
        print("S")
        Stop()
    if letter == "e":
        print("E")
        Exit()

#Right(.07)
#Forward(1)
#Stop()
#GPIO.cleanup()

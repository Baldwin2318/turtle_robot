#libriries
from time import sleep_us
from time import sleep_ms
from machine import Pin

cw = 1
ccw =0
MotL_Dir = Pin(14,Pin.OUT)
MotL_Step = Pin(12,Pin.OUT)

MotR_Dir = Pin(26,Pin.OUT)
MotR_Step = Pin(27,Pin.OUT)

Full_step = 200
Circonference_wheel = 204.2
steps_per_mm = Full_step / Circonference_wheel

def moveLeftMot (step, speed):
    for i in range(step):
        MotL_Step.value(1)
        sleep_us(speed)
        MotL_Step.value(0)
        sleep_us(speed)
        
def moveRightMot (step, speed):
    for i in range(step):
        MotR_Step.value(1)
        sleep_us(speed)
        MotR_Step.value(0)
        sleep_us(speed)
        
def moveForward (j):
    for i in range(j):
        MotL_Dir.value(ccw)
        moveLeftMot(1, 500)
        MotR_Dir.value(cw)
        moveRightMot(1, 500)

def movebackward (i):
    for i in range(i):
        MotL_Dir.value(cw)
        moveLeftMot(1, 3000)
        MotR_Dir.value(ccw)
        moveRightMot(1, 3000)

def rotation_circle (j):
    for i in range(j):
        moveLeftMot(1, 5000, cw)
        
def TurnLeft(dist): 
    convertstep = round(dist * steps_per_mm) 
    for i in range(convertstep):
        MotL_Dir.value(ccw)
        moveLeftMot(1, 1000)
        MotR_Dir.value(ccw)
        moveRightMot(1, 1000)
        
def TurnRight(dist): 
    convertstep = round(dist * steps_per_mm)
    for i in range(convertstep):
        MotL_Dir.value(cw)
        moveLeftMot(1, 300) #1000
        MotR_Dir.value(cw)
        moveRightMot(1, 300)



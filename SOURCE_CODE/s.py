from machine import Pin, PWM

servo = (PWM(Pin(33), freq = 50))

def PenDown():
    servo.duty(130)
    
def PenUp():
    servo.duty(80)

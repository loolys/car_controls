from pyfirmata import Arduino, util
import time

board = Arduino('COM3')

forward = board.get_pin('d:9')
reverse = board.get_pin('d:10')
left = board.get_pin('d:11')
right = board.get_pin('d:12')

def go_forward():
    reverse.write(0)
    forward.write(1)
    
def go_reverse():
    forward.write(0)
    reverse.write(1)
    
def go_left():
    right.write(0)
    left.write(1)
    
def go_right():
    left.write(0)
    right.write(1)
    
def stop_car():
    forward.write(0)
    reverse.write(0)
    left.write(0)
    right.write(0)
    
while True:
    go_forward()
    time.sleep(1)
    go_right()
    time.sleep(0.5)
    go_left()
    time.sleep(0.5)
    go_reverse()
    time.sleep(1)
    stop_car()
    time.sleep(2)
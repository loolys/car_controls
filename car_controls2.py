from pyfirmata import Arduino, util
import time

class CarControls:
    board = Arduino('COM3')

    self.forward = board.get_pin('d:9:o')
    self.reverse = board.get_pin('d:10:o')
    self.left = board.get_pin('d:11:o')
    self.right = board.get_pin('d:6:o')

    def go_forward(self):
        self.reverse.write(0)
        self.forward.write(1)
        
    def go_reverse(self):
        self.forward.write(0)
        self.reverse.write(1)
        
    def go_left(self):
        self.right.write(0)
        self.left.write(1)
        
    def go_right(self):
        self.left.write(0)
        self.right.write(1)
        
    def stop_car(self):
        self.forward.write(0)
        self.reverse.write(0)
        self.left.write(0)
        self.right.write(0)
        
        
    def read_state(self, button):
        if button == "forward":
            return self.forward.read()
        elif button == "reverse":
            return self.reverse.read()
        elif button == "left":
            return self.left.read()
        elif button == "right":
            return self.right.read()
        else:
            return "error"
    

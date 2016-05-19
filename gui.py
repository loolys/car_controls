import tkinter
from car_controls2 import CarControls

class Gui:

    def forward_press(self):
        self.carControls.go_forward()
        self.update_labels()
        
    def reverse_press(self):
        self.carControls.go_reverse()
        self.update_labels()
        
    def left_press(self):
        self.carControls.go_left()
        self.update_labels()
    
    def right_press(self):
        self.carControls.go_right()
        self.update_labels()
    
    def stop_press(self):
        self.carControls.stop_car()
        self.update_labels()

    def update_labels(self):
        self.forward_label.configure(text=self.carControls.read_state("forward"))
        self.reverse_label.configure(text=self.carControls.read_state("reverse"))
        self.left_label.configure(text=self.carControls.read_state("left"))
        self.right_label.configure(text=self.carControls.read_state("right"))
        
    def __init__(self):
        self.carControls = CarControls()
        window = tkinter.Tk()
        window.geometry("100x220")
        
        self.forward_button = tkinter.Button(window, text="Forward", command=self.forward_press)
        self.reverse_button = tkinter.Button(window, text="Reverse", command=self.reverse_press)
        self.left_button = tkinter.Button(window, text="Left", command=self.left_press)
        self.right_button = tkinter.Button(window, text="Right", command=self.right_press)
        self.stop_button = tkinter.Button(window, text="Stop", command=self.stop_press)
        
        self.forward_label = tkinter.Label(window, text=self.carControls.read_state("forward"))
        self.reverse_label = tkinter.Label(window, text=self.carControls.read_state("reverse"))
        self.left_label = tkinter.Label(window, text=self.carControls.read_state("left"))
        self.right_label = tkinter.Label(window, text=self.carControls.read_state("right"))
        
        self.forward_button.pack()
        self.forward_label.pack()
        self.reverse_button.pack()
        self.reverse_label.pack()
        self.left_button.pack()
        self.left_label.pack()
        self.right_button.pack()
        self.right_label.pack()
        self.stop_button.pack()
        window.mainloop()
        
    
if __name__ == "__main__":
    Gui()
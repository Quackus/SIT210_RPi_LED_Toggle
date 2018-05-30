from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
                           
button = IntVar()                          

def ledToggle():
    print(button.get())
    led1.off()
    led2.off()
    led3.off()
    if button.get() == 1:
        led1.on()
    elif button.get() == 2:
        led2.on()
    elif button.get() == 3:
        led3.on()
    

led1Button = Radiobutton(win, text = 'Turn LED 1 On', font = myFont, command = ledToggle, variable = button, value = 1, bg = 'bisque2', height = 1, width = 24)
led1Button.grid(row=0,column=1)

led2Button = Radiobutton(win, text = 'Turn LED 2 On', font = myFont, command = ledToggle, variable = button, value = 2, bg = 'bisque2', height = 1, width = 24)
led2Button.grid(row=1,column=1)

led3Button = Radiobutton(win, text = 'Turn LED 3 On', font = myFont, command = ledToggle, variable = button, value = 3, bg = 'bisque2', height = 1, width = 24)
led3Button.grid(row=2,column=1)

offButton = Radiobutton(win, text = 'Off', font = myFont, command = ledToggle, variable = button, value = 0, bg = 'bisque2', height = 1, width = 24)
offButton.grid(row=3,column=1)
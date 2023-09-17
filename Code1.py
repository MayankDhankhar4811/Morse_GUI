from tkinter import *
import RPi.GPIO as GPIO
from time import *
from gpiozero import LED 
GPIO.setmode(GPIO.BCM)

### LED PINS ###
Led =14

# SETUP FOR PINS
GPIO.setup(Led, GPIO.OUT)
GPIO.output(Led, GPIO.LOW)

# GUI definitions
win = Tk()
win.title("Morse Blinking")
win['background']='blue'
myFont=tkinter.font.Font(family='Arial',size=12,weight="bold")

### LED Functions ###

# Function for dot command providing small blinking interval
def dot():
    GPIO.output(Led, GPIO.HIGH)
    sleep(0.25) # Time delay for 0.25 seconds
    GPIO.output(Led, GPIO.LOW)
    sleep(0.25) # Time delay for 0.25 seconds

# Function for dash command providing longer blinking duration
def dash():
    GPIO.output(Led, GPIO.HIGH)
    sleep(1.5)  # Time delay for 1.5 seconds
    GPIO.output(Led, GPIO.LOW)
    sleep(0.25) # Time delay for 0.25 seconds


# Defining morse combination for individual characters
def a():
    dot()
    dash()

def b():
    dash()
    dot()
    dot()
    dot()

def c():
    dash()
    dot()
    dash()
    dot()

def d():
    dash()
    dot()
    dot()

def e():
    dot()

def f():
    dot()
    dot()
    dash()
    dot()

def g():
    dash()
    dash()
    dot()

def h():
    dot()
    dot()
    dot()
    dot()

def i():
    dot()
    dot()

def j():
    dot()
    dash()
    dash()
    dash()

def k():
    dash()
    dot()
    dash()

def l():
    dot()
    dash()
    dot()
    dot()

def m():
    dash()
    dash()

def n():
    dash()
    dot()

def o():
    dash()
    dash()
    dash()

def p():
    dot()
    dash()
    dash()
    dot()

def q():
    dash()
    dash()
    dot()
    dash()

def r():
    dot()
    dash()
    dot()

def s():
    dot()
    dot()
    dot()

def t():
    dash()

def u():
    dot()
    dot()
    dash()

def v():
    dot()
    dot()
    dot()
    dash()

def w():
    dot()
    dash()
    dash()

def x():
    dash()
    dot()
    dot()
    dash()

def y():
    dash()
    dot()
    dash()
    dash()

def z():
    dash()
    dash()
    dot()
    dot()

#Code for EXIT
def close():
    GPIO.cleanup
    win.destroy()   

# Function for morse code conversion
def morse_encryption():
    name = entryBox.get()
    length = len(name)
    counter = 0
    labelActive = False;

    if length > 12:
        close()

    else:
        for letter in name:
            if letter == "a":
                a()
                continue
            elif letter == "b":
                b()
                continue
            elif letter == "c":
                c()
                continue
            elif letter == "d":
                d()
                continue
            elif letter == "e":
                e()
                continue
            elif letter == "f":
                f()
                continue
            elif letter == "g":
                g()
                continue
            elif letter == "h":
                h()
                continue
            elif letter == "i":
                i()
                continue
            elif letter == "j":
                j()
                continue
            elif letter == "k":
                k()
                continue
            elif letter == "l":
                l()
                continue
            elif letter == "m":
                m()
                continue
            elif letter == "n":
                n()
                continue
            elif letter == "o":
                o()
                continue
            elif letter == "p":
                p()
                continue
            elif letter == "q":
                q()
                continue
            elif letter == "r":
                r()
                continue
            elif letter == "s":
                s()
                continue
            elif letter == "t":
                t()
                continue
            elif letter == "u":
                u()
                continue
            elif letter == "v":
                v()
                continue
            elif letter == "w":
                w()
                continue
            elif letter == "x":
                x()
                continue
            elif letter == "y":
                y()
                continue
            elif letter == "z":
                z()
                continue
            

        

### BUTTONS FOR LED ###
BoxLabel = Label(win, text = 'Enter a name to display in morse code (12 characters max)',font=myFont)
BoxLabel.grid(row = 0, column = 0)

Box = Entry(win)
Box.grid(row = 2, column = 3)

submitButton = Button(win, text = "BLINK LED",font=myFont, command = morse_encryption,bg='green',fg='white')
submitButton.grid(row = 4, column = 3)

exitButton = Button(win, text = "EXIT WINDOW",font=myFont, command = close,bg='red',fg='white')
exitButton.grid(row = 6, column = 3)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop() #Loop forever
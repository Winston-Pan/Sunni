import RPi.GPIO as g
import drive
g.setmode(g.BOARD)
g.setup(35,g.OUT)#in 1
g.setup(36,g.OUT)#in 2
g.setup(37,g.OUT)#in 3
g.setup(38,g.OUT)#in 4
g.setup(15,g.IN)
g.setup(29,g.IN)
g.setup(31,g.IN)
g.setup(33,g.IN)
g.output(35,False)
g.output(37,False)
g.output(36,False)
g.output(38,False)

while True:
    if g.input(29)==True:
        drive.turn_right(0.5,35,36,37,38)

    if g.input(31)==True:
        drive.turn_left(0.5,35,36,37,38)

    if g.input(15)==True:
        drive.turn_right(1,35,36,37,38)

    if g.input(33)==True:
        drive.turn_left(1,35,36,37,38)

    if g.input(29)==False:
        drive.forward(1,35,36,37,38)

    if g.input(31)==False:
        drive .forward(1,35,36,37,38)

    if g.input(15)==False:
        drive.forward(1,35,36,37,38)

    if g.input(33)==False:
        drive.forward(1,35,36,37,38)

g.cleanup()

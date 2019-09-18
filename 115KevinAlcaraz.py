#   a115_buggy_image.py
import turtle as trtl

drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)
sticks = 6
length = 70
legangle = 380 / sticks
drawer.pensize(5)
counter = 0
while (counter < sticks):
  drawer.goto(0,0)
  drawer.setheading(legangle*counter)
  drawer.forward(length)
  counter = counter + 1

drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop()
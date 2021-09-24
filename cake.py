import turtle
t = turtle.Turtle()

def triangle(len):
  for i in range(3):
    t.forward(len)
    t.left(120)

def rectangle(width, height):
  for i in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)

def lg_cake():
  for i in range(3):
    rectangle(30,310)
    t.forward(30)

def sm_cake():
  for i in range(3):
    rectangle(35,210)
    t.forward(35)

def main():

  t.speed(0)
  t.color("purple")

#first triangle  
  t.begin_fill()
  triangle(90)
  t.end_fill()
  
#movement for the first cake
  t.penup()
  t.forward(200)
  t.right(90)
  t.forward(4)
  t.pendown()

  lg_cake()

#movement towards the second cake
  t.penup()
  t.forward(5)
  t.left(90)
  t.forward(210)
  t.left(90)
  t.forward(90)

  t.pendown()
  t.color("green")
  t.right(90)

  t.begin_fill()
  triangle(90)
  t.end_fill()

  t.penup()
  t.forward(150)
  t.right(90)
  t.forward(4)
  t.pendown()

  sm_cake()

main()


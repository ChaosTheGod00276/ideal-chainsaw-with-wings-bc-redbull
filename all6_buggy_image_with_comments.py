import turtle as trtl

# Initialize the turtle to draw the spider
spider = trtl.Turtle()

# Create a spider body
spider.pensize(60)
spider.circle(30)

# Draw a spider head
spider.penup()
spider.goto(0,-60)
spider.pendown()
spider.pensize(40)
spider.circle(20)

# Configure spider legs
num_legs = 8
legs_per_side = num_legs // 2
length_legs = 70
spread_angle = 60
angle_between = (spread_angle / (legs_per_side - 1)) + 5

spider.pensize(5)

# Draw left side legs
for leg_num in range(legs_per_side):
    spider.penup()
    spider.goto(0, 15)
    spider.pendown()
    angle = 180 + (-spread_angle/2 + leg_num * angle_between)
    spider.setheading(angle - 45)
    spider.circle(100, 180,3)

# Draw right side legs
for leg_num in range(legs_per_side):
    spider.penup()
    spider.goto(0, 15)
    spider.pendown()
    angle = ( -spread_angle/2 + leg_num * angle_between )
    spider.setheading(angle + 45)
    spider.circle(-100,180,3)

# Draw eyes
spider.penup()
spider.goto(-20,-50)
spider.pendown()
spider.pensize(6)
spider.pencolor("red")
for i in range(2):
  spider.pendown()
  spider.circle(3)
  spider.penup()
  spider.setheading(0)
  spider.forward(40)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
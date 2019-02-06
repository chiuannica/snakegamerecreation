import random
import time
import turtle

delay = 0.1

# Score
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("pink")
wn.setup(width=600, height=600)
wn.tracer(0)            #turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)           #no slow down for animation
head.shape("square")
head.color("white")
head.penup()            #do not draw line
head.goto(0,0)          #starts in the middle
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)           #no slow down for animation
food.shape("circle")
food.color("hotpink")
food.penup()            #do not draw line
food.goto(0,100)

segments = []           #add segment to list every time snake eats food

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:             #repeats 5ever, makes the game work
    wn.update()

    # Check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000) #moving segments very far away

        # Clear segments list
        segments.clear()

        # Reset the score
        score = 0

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # Check for collision with food
    if head.distance(food) < 20:
        # Move food to random spot
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x,y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightblue")
        new_segment.penup()
        segments.append(new_segment) #adds new segment to list

        # Increase score
        score += 10
        
        # Update display
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    move()

    # Check for head collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000) #moving segments very far away

            # Clear segments list
            segments.clear()

            # Reset the score
            score = 0

            # Update display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)   #stops program for 0.1 seconds
#keeps window open
wn.mainloop()

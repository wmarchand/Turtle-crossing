from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.setheading(90)
        #self.move_speed = 0.1

    def up(self):
        # new_y =  self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(),new_y)
        self.forward(MOVE_DISTANCE)

    def down(self):
        # new_y =  self.ycor() - MOVE_DISTANCE
        # self.goto(self.xcor(),new_y)
        self.backward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self):
        self.goto(STARTING_POSITION)
        #self.move_speed *= 0.9
        

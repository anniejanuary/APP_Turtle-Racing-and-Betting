from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
# size of the screen #BEST TO USE KEYWORD ARGUMENTS RATHER THAN POSITIONAL ARGUMENTS (just (500, 400))
# HERE to know wha;s what

class RaceClass:

    def __init__(self):
        self.turtle_colors = ["red", "purple", "blue", "pink", "orange", "green"]
        self.turtles = []
        self.games_played = 0
        self.games_won = 0
        for i in range(len(self.turtle_colors)):
            self.turtles.append(Turtle(shape="turtle"))
            self.turtles[i].color(self.turtle_colors[i])
        draw_finish_line = Turtle()
        draw_finish_line.hideturtle()
        draw_finish_line.pu()
        draw_finish_line.goto(x=190, y=150)
        draw_finish_line.color("black")
        draw_finish_line.pd()
        draw_finish_line.goto(x=190, y=-150)
        self.score_turtle = Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.pu()
        self.score_title_turtle = Turtle()
        self.score_title_turtle.hideturtle()
        self.score_title_turtle.pu()
        self.score_title_turtle.goto(x=0, y=200)
        self.score_title_turtle.color("black")
        self.score_title_turtle.pd()
        style1 = ('Franklin Gothic Book', 15, 'bold')
        self.score_title_turtle.write(f"Current score: ", font=style1, align='center')
        self.score_title_turtle.pu()

    def turtles_position(self, x, y):
        for t in self.turtles:
            t.pu()
            t.goto(x, y)
            y += 40

    def user_bet(self):
        self.bet = screen.textinput(title="Enter your bet", prompt="Which turtle will win the race?: ")

    def start_race(self):
        finish_line = False
        while not finish_line:
            for t in self.turtles:
                random_steps = random.randint(0, 10)
                t.forward(random_steps)
                if t.xcor() >= 172:
                    finish_line = True
                    self.winner = self.turtle_colors[self.turtles.index(t)]

    def text(self, x, y):
        self.message = Turtle()
        self.message.hideturtle()
        self.message.pu()
        self.message.goto(x, y)
        self.message.speed("slowest")
        self.message.color('black')
        style1 = ('Franklin Gothic Book', 15, 'bold')
        style2 = ('Franklin Gothic Book', 12)
        self.message.pd()
        self.message.write(f"{self.winner.title()} turtle won!", font=style1, align='center')
        self.message.pu()
        self.message.goto(x, y-30)
        self.message.pd()
        self.games_played += 1
        if self.bet == self.winner:
            self.message.write("Your bet won!", font=style1, align='center')
            self.games_won += 1
        else:
            self.message.write("Sorry, better luck next time!", font=style1, align='center')
        race.score()
        self.message.pu()
        self.message.goto(x, y-90)
        self.message.pd()
        self.message.write("Click anywhere to play again / press 'q' to exit", font=style2, align='center')
        self.message.hideturtle()

    def score(self):
        self.score_turtle.clear()
        self.score_turtle.reset()
        self.score_turtle.hideturtle()
        self.score_turtle.pu()
        style1 = ('Franklin Gothic Book', 15, 'bold')
        self.score_turtle.goto(x=100, y=200)
        self.score_turtle.color("black")
        self.score_turtle.pd()
        self.score_turtle.write(f"{self.games_won}/{self.games_played}", font=style1, align='center')
        self.score_turtle.pu()


    def restart(self, mouseclickx, mouseclicky):
                        # why these "mouseclickx, mouseclicky" are needed:
                        # https://stackoverflow.com/questions/48869611/turtle-onscreenclick-not-behaving-as-expected
        self.turtles_position(x=-230, y=-100)
        self.message.clear()
        race.user_bet()
        if race.user_bet:
            race.start_race()
            if race.text(x=0, y=-170):
                screen.listen()
                screen.onkey(screen.bye, "q")  # Register function exit to event "q" key press
                screen.onclick(fun=race.restart)
                race.user_bet()


race = RaceClass()
race.turtles_position(x=-230, y=-100)
race.user_bet()
if race.user_bet:
    race.start_race()
    race.text(x=0, y=-170)
    screen.listen()
    screen.onkey(screen.bye, "q")  # Register function exit to event "q" key press
    screen.onclick(fun=race.restart)
screen.mainloop()




from turtle import Turtle
from high_score_tracker import HighScoreTracker

ALIGN_CENTER = "center"
ALIGN_LEFT = "left"
ALIGN_RIGHT = "right"

FONT = font=('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self, tracker: HighScoreTracker | None = None):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

        self.score = 0
        self. tracker = tracker or HighScoreTracker()

        self.high_writer = Turtle()
        self.high_writer.hideturtle()
        self.high_writer.color("white")
        self.high_writer.penup()
        
        self._draw_hud()

    def _draw_hud(self):
        self.clear()
        self.high_writer.clear()

        self.goto(-280, 270)
        self.write(f"Score: {self.score}", move=False, align=ALIGN_LEFT, font=FONT)

        self.high_writer.goto(280, 270)
        self.high_writer.write(f"High: {self.tracker.get()}", move=False, align=ALIGN_RIGHT, font=FONT)
    

    def game_over(self):
        if self.tracker.maybe_update(self.score) == True:
            self.new_highscore()

        message = Turtle()
        message.goto(0,0)
        message.color("red")
        message.hideturtle()
        
        message.penup()
        
        message.write("GAME OVER" ,move=False, align = ALIGN_CENTER, font = FONT)

    def new_highscore(self):

        message = Turtle()
        message.goto(0,-36)
        message.color("gold")
        message.hideturtle()
        
        message.penup()
        
        message.write(f"NEW HIGH SCORE: {self.score}" ,move=False, align = ALIGN_CENTER, font = FONT)
    

    def increase_score(self):
        self.score += 1
        self._draw_hud()
    
    def reset_score(self):
        self.score = 0
        self._draw_hud()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}" ,move=False, align = ALIGN_CENTER, font = FONT)


    

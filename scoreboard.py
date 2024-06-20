from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Load the high score from a file
        with open("highscore.txt") as highscore:
            self.high_score = int(highscore.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Update the scoreboard display
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        # Update the high score if necessary and reset the current score
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

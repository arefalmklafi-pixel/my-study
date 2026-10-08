
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.clock import Clock
from random import choice

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.lives = 3
        self.ball_x = 200
        self.ball_y = 180
        self.dx = 220
        self.dy = -250
        self.paddle_x = 150
        self.bricks = []
        self.game_over = False
        self.make_bricks()
        Clock.schedule_interval(self.update, 1 / 60)

    def make_bricks(self):
        self.bricks = []
        for row in range(5):
            for col in range(6):
                self.bricks.append([
                    10 + col * 64,
                    400 + row * 25,
                    58,
                    18
                ])

    def on_touch_down(self, touch):
        self.paddle_x = touch.x
        if self.game_over:
            self.score = 0
            self.lives = 3
            self.ball_x = self.width / 2
            self.ball_y = 180
            self.dx = 220
            self.dy = -250
            self.game_over = False
            self.make_bricks()
        return True

    def on_touch_move(self, touch):
        self.paddle_x = touch.x
        return True

    def update(self, dt):
        if self.width <= 0 or self.height <= 0:
            return

        if not self.game_over:
            self.ball_x += self.dx * dt
            self.ball_y += self.dy * dt

            if self.ball_x < 7 or self.ball_x > self.width - 7:
                self.dx *= -1

            if self.ball_y > self.height - 45:
                self.dy = -abs(self.dy)

            if (self.ball_y < 60 and self.dy < 0
                    and abs(self.ball_x - self.paddle_x) < 65):
                self.dy = abs(self.dy)

            for brick in self.bricks[:]:
                x, y, w, h = brick
                if x <= self.ball_x <= x + w and y <= self.ball_y <= y + h:
                    self.bricks.remove(brick)
                    self.dy *= -1
                    self.score += 10
                    break

            if self.ball_y < 0:
                self.lives -= 1
                if self.lives <= 0:
                    self.game_over = True
                else:
                    self.ball_x = self.width / 2
                    self.ball_y = 180
                    self.dy = abs(self.dy)

            if not self.bricks:
                self.game_over = True

        self.canvas.clear()
        with self.canvas:
            Color(0.04, 0.06, 0.15, 1)
            Rectangle(pos=self.pos, size=self.size)

            Color(1, 1, 1, 1)
            for i, brick in enumerate(self.bricks):
                Color(1, 0.3 + (i % 3) * 0.2, 0.2, 1)
                Rectangle(pos=brick[:2], size=brick[2:])

            Color(0.2, 0.6, 1, 1)
            Rectangle(pos=(self.paddle_x - 50, 35), size=(100, 15))

            Color(1, 1, 1, 1)
            Ellipse(pos=(self.ball_x - 7, self.ball_y - 7), size=(14, 14))

class BrickBreakerApp(App):
    def build(self):
        self.title = "Brick Breaker"
        return Game()

BrickBreakerApp().run()

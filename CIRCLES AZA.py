import pygame
from pygame.draw import circle, lines
from random import randint

pygame.init()

FPS = 300
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self, x, y, r, vx=0, vy=0, color=-1):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        if color == -1:
            self.color = COLORS[randint(0, 5)]
        else:
            self.color = color

    def move(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def coordinate(self):
        print(self.x, self.y)

    def collision(self):
        if self.x > WIDTH - self.r or self.x < self.r:
            self.vx *= -1
        if self.y > HEIGHT - self.r or self.y < self.r:
            self.vy *= -1

    # выдает тру если клик был по шарику
    def eventmouse(self, event):
        pos_x, pos_y = event.pos
        return (pos_x - self.x) ** 2 + (pos_y - self.y) ** 2 <= self.r ** 2


def new_ball():
    '''создает обычный шарик '''
    x = randint(100, 400)
    y = randint(100, 400)
    r = randint(40, 60)
    vx = randint(30, 500)
    vy = randint(30, 500)
    color = COLORS[randint(0, 5)]
    ball = Ball(x, y, r, vx, vy)
    return ball


def speed_ball():
    '''создает скоростной шарик '''
    x = randint(100, 400)
    y = randint(100, 400)
    r = randint(20, 30)
    vx = randint(2000, 3000) / 100
    vy = randint(2000, 3000) / 100
    color = WHITE
    speed = Ball(x, y, r, vx, vy, WHITE)
    return speed


def score_for_ball(balls, event):
    for ball in balls:
        if ball.eventmouse(event):
            if ball.r < 40:
                balls.remove(ball)
                balls.append([speed_ball(),new_ball()][randint(0,1)])
                return 10
            else:
                balls.remove(ball)
                balls.append([speed_ball(), new_ball()][randint(0, 1)])
                return 1
    return 0


# массив шариков
balls = []
for i in range(8):
    balls.append(new_ball())
for i in range(1):
    balls.append(speed_ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

a = 0
b = 5
while not finished:
    c = [new_ball(), speed_ball()][randint(0, 1)]
    clock.tick(FPS)
    for i in balls:
        i.move(1 / FPS)
        i.collision()
        i.draw()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            e=score_for_ball(balls, event)
            a += e
            if e == 0:
                b -= 1
            if b == 0:
                print('ИГРА ОКОНЧЕНА')
                print('количество очков =', a)
                finished = True

        if event.type == pygame.QUIT:
            print('ИГРА ОКОНЧЕНА')
            print('количество очков =', a)
            finished = True
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

import math
from random import choice
from random import randint
import pygame

FPS = 300

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=15, y = HEIGHT - 10):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME

        #kx - коэфицент отскока от стен
        kx = 0.75
        #ky - коэфицент отскока от пола
        ky = 0.75
        dt = 10/FPS
        g = -10
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt
        if self.x < self.r:
            self.vx *= -kx
            self.x = self.r
        if self.x > WIDTH - self.r:
            self.x = WIDTH - self.r
            self.vx *= -kx
        if self.y < HEIGHT - self.r:
            self.vy = self.vy - g*0.1
            if self.y < self.r:
                self.vy *= -1
        if self.y > HEIGHT - self.r:
            self.vy *= -ky
            self.y = HEIGHT - self.r




    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        return (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 < (self.r + obj.r - 5)**2


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 3
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = (self.f2_power * math.cos(self.an))*2.75
        new_ball.vy = -(self.f2_power * math.sin(self.an))*2.75
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.circle(screen, self.color, (10, HEIGHT-10), 10)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, r, vx, vy, color, x, y, zx, zy):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        self.vx = vx
        self.vy = vy
        self.live = 1
        self.zx = zx
        self.zy = zy
    # FIXME: don't work!!! How to call this functions when object is created?
    def move_target(self):
        self.x += self.vx
        self.y += self.vy
    def collitionon_target(self):
        if self.x < self.r:
            self.x = self.r
            self.vx *= -1
        if self.x > WIDTH - self.r:
            self.x = WIDTH - self.r
            self.vx *= -1
        if self.y < self.r:
            self.vy *= -1
        if self.y > HEIGHT * 0.75:
            self.vy *= -1
            self.y = HEIGHT * 0.75
    def unusuall_traektory(self):
        delta = 200
        if self.x < self.zx:
            self.x = self.zx
            self.vx *= -1
        if self.x > self.zx + delta:
            self.x = self.zx + delta
            self.vx *= -1
        if self.y < self.zy:
            self.y = self.zy
            self.vy *= -1
        if self.y > self.zy + delta:
            self.y = self.zy + delta
            self.vy *= -1



    def new_target(self):
        self.x = randint(60, 500)
        self.y = randint(60, 550)
        self.r = randint(30, 50)
        self.zx = randint(60, 759)
        self.zy = randint(60, 529)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
    def count_points(self):
        print('ИГРА ОКОНЧЕНА.КОЛИЧЕСТВО ОЧКОВ :', self.points)
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
def TARGET_ONE():
    color = BLACK
    vx = 0.5
    vy = 0.5
    xx = 0
    yy = 0
    r = randint(40, 50)
    x = randint(600, 780)
    y = randint(300, 550)
    targ1 = Target(r, vx, vy, color, x, y, xx, yy)
    return targ1
def TARGET_TWO():
    color = BLACK
    vx = 4
    vy = 4
    r = randint(10, 20)
    x = randint(60, 780)
    zx = randint(60, 759)
    zy = randint(60, 529)
    # зная начальное положение по x по y зададим движение в пределах квадрата
    y = randint(60, 550)

    targ2 = Target(r, vx, vy, color, x, y, zx, zy)
    return targ2
#создам массив из начальных координат


# создаю массив чтобы потом по нему итерироваться
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
a = TARGET_ONE()
b = TARGET_TWO()
finished = False
goals = 0
while not finished:
    screen.fill(WHITE)
    gun.draw()
    a.collitionon_target()
    b.collitionon_target()
    b.unusuall_traektory()
    a.move_target()
    b.move_target()
    a.draw()
    b.draw()
    for x in balls:
        x.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('ИГРА ОКОНЧЕНА, КОЛИЧЕСТВО ОЧКОВ :', goals)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for x in balls:
        x.move()
        if x.hittest(a):
            goals += 1
            a.new_target()
        if x.hittest(b):
            goals += 1
            b.new_target()

    gun.power_up()

pygame.quit()
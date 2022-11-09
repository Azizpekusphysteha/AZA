import pygame
import pygame as pg
pg.init
sc=pg.display.set_mode((600,400))
black=(0,0,0)
red=(255,0,0)
yellow=(255,250,0)
pg.draw.circle(sc,yellow,(295,180),150)
pg.draw.circle(sc,red,(350,130),20)
pg.draw.circle(sc,black,(350,130),10)
pg.draw.circle(sc,red,(240,130),25)
pg.draw.circle(sc,black,(240,130),15)
pg.draw.line(sc,black,(190,80),(280,100),20)
pg.draw.line(sc,black,(400,80),(310,100),20)
pg.draw.rect(sc,black,(233,260,130,20))
pg.display.flip()
while True:
    for event in pg.event.get():
        if event.type==pygame.QUIT:
            exit()


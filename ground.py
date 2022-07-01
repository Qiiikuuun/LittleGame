import pgzrun
import random

# 地面坦克小游戏，900*600

things = []
bomb = []
attack = []
defend = []

player = Actor("tank")
player.center = 200, 580
player.score = 0
plane = Actor("helicopter")
plane.center = 200, 100
tank = Actor("tank1")
tank.center = 800, 550
fly=0
go=0
rank=1

WIDTH = 900
HEIGHT = 600

def draw():
    screen.clear()
    screen.blit("backg2", (0, 0))
    for t in things:
        t.draw()
    for t in attack:
        t.draw()
    for t in defend:
        t.draw()
    player.draw()
    plane.draw()
    tank.draw()
    global rank 
    screen.draw.text("SCORE:%d, ENEMY:%d" % (player.score,4-rank),(360, 10),fontsize=30, color='black')
    screen.draw.text("click to fire,you can destroy an enemy when get 20 points",(240, 30),fontsize=30, color='black')


def update():
    global rank
    if player.score>=20 and rank == 1:
        rank = 2
        tank.image = "destroy"
        sounds.des.play()
        clock.schedule_unique(set_tank2, 1.0)
    if player.score>=40 and rank == 2:
        rank = 3
        tank.image = "destroy"
        sounds.des.play()
        clock.schedule_unique(set_tank3, 2.0)
    if player.score>60:
        rank = 4
#此行用于转入下一个场景的游戏
    global fly
    plane.x+=fly
    if plane.x<50:
        fly=3
    if plane.x>550:
        fly=-3
    if random.randrange(180-40*rank) == 0:
        fly=random.uniform(-4,4)
        t = Actor("bomb")
        t.center = plane.x, 120
        things.append(t)
    for t in things:
        t.y += (1+rank)
        if t.y >= 600:
            things.remove(t)
        elif t.colliderect(player):
            things.remove(t)
            player.score -= 4
            sounds.exp.play()
    global go
    tank.y+=go
    if tank.y<430:
        go=3
    if tank.y>590:
        go=-3
    if random.randrange(140-30*rank) == 0:
        go=random.uniform(-4,4)
        t = Actor("attack")
        t.center = 760,tank.y-20
        attack.append(t)
    for t in attack:
        t.x -= (1+rank)
        if t.x <= 0:
            attack.remove(t)
        elif t.colliderect(player):
            attack.remove(t)
            player.score -= 4
            sounds.exp.play()
    for t in defend:
        t.x += 4
        if t.x >= 900:
            defend.remove(t)
        elif t.colliderect(tank):
            defend.remove(t)
            player.score += 1
            sounds.blip.play()

def on_mouse_move(pos):
    if pos[0]<600:
        player.x = pos[0]
    if 400<pos[1]:
        player.y=pos[1]
        
def on_mouse_down(pos):
    t = Actor("defend")
    t.center = player.x+50,player.y-20
    defend.append(t)


def set_tank2():
    tank.image = "tank2"
def set_tank3():
    tank.image = "tank3"

pgzrun.go()

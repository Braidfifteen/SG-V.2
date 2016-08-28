import pygame as pg
import prepare as p
import roombuild as rb

class Room():
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.power_up_list = pg.sprite.Group()
        self.bullet_list = pg.sprite.Group()
        self.enemy_list = pg.sprite.Group()
        self.wall_list = pg.sprite.Group()
        self.teleporter_list = pg.Sprite.Group()
        self.border = rb.RoomBorders()
        self.doors = rb.RoomDoors()
        
class Room_0(Room):
    def __init__(self, player):
        super().__init__(player)
        
        walls = [[300, 200, 50, 350, RED],
                 [250, 600, 450, 50, RED],
                 [650, 350, 50, 350, RED],
                 [650, 350, 350, 50, RED],
                 [900, 200, 50, 450, RED],
                 [1500, 150, 50, 250, RED],
                 [1200, 800, 500, 50, RED]
                ]
 
        # Walls
        for i in walls:
            wall = rb.Wall(self, self.game, i[0], i[1], i[2], i[3], i[4])
        
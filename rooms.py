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
        self.teleporter_list = pg.sprite.Group()
        self.borders = rb.RoomBorders()
        self.doors = rb.RoomDoors()
        
class Room_0(Room):
    def __init__(self, game, player):
        super().__init__(game, player)
        
        walls = [[300, 200, 50, 350, p.RED],
                 [250, 600, 450, 50, p.RED],
                 [650, 350, 50, 350, p.RED],
                 [650, 350, 350, 50, p.RED],
                 [900, 200, 50, 450, p.RED],
                 [1500, 150, 50, 250, p.RED],
                 [1200, 800, 500, 50, p.RED]
                ]
 
        # Walls
        for i in walls:
            wall = rb.Wall(self, self.game, i[0], i[1], i[2], i[3], i[4])
            
        # Doors
        for i in self.doors.left_door(p.RED):
            self.door1 = rb.Wall(self, self.game, i[0], i[1], i[2], i[3], i[4])
        for i in self.doors.right_door(p.RED):
            self.door2 = rb.Wall(self, self.game, i[0], i[1], i[2], i[3], i[4])
            
        # Borders
        for i in self.borders.left_right_door(p.BLUE):
            border = rb.Wall(self, self.game, i[0], i[1], i[2], i[3], i[4])
            
            
def create_room_list(game, player):
    room_list = []
    room = Room_0(game, player)
    room_list.append(room)
    return room_list
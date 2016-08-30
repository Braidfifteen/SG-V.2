import pygame as pg
import prepare as p
import roombuild as rb
import random

class Room():
    def __init__(self, game, player, borders):
        self.game = game
        self.player = player
        self.power_up_list = pg.sprite.Group()
        self.bullet_list = pg.sprite.Group()
        self.enemy_list = pg.sprite.Group()
        self.wall_list = pg.sprite.Group()
        self.teleporter_list = pg.sprite.Group()
        self.borders = borders
        self.doors = rb.RoomDoors()
        self.border_list(self.borders)
        
    def border_list(self, borders):
        for i in borders:
            border = rb.Wall(self, self.game, i[0], i[1], i[2], i[3], i[4])
            
        
        
        
        
class CreateRooms():
    def __init__(self, game, player):
        super().__init__()
        self.room_list = None
        self.room_no_list = self.create_layout()
        self.game = game
        self.player = player
        
    def create_layout(self):
        count = 0
        array = []
        while count <= random.randint(10, 15):
            rand = random.randint(0, 19)
            if count <= 0:
                array.append(rand)
                count += 1
            elif count >= 1:
                if rand == array[count-1] + 5 and rand not in array:
                    array.append(rand)
                    count += 1
                elif rand == array[count-1] - 5 and rand not in array:
                    array.append(rand)
                    count += 1
                elif rand == array[count-1] + 1 and rand not in array:
                    array.append(rand)
                    count += 1
                elif rand == array[count-1] - 1 and rand not in array:
                    array.append(rand)
                    count += 1
                else:
                    pass
        return array
    
    def floor_grid(self, room_no_list):
        grid_list = []
        for i in range(20):
            grid_list.append(0)
        for i in room_no_list:
            grid_list[i] = 1
        return grid_list
    
    def make_rooms(self):
        room_list = self.floor_grid(self.room_no_list)
        for i in range(len(room_list)):
            if room_list[i] == 1:
                borders = self.make_borders(i, room_list)
                room_list[i] = Room(self.game, self.player, borders)
        return room_list

            
    def make_borders(self, i, floor_grid):
        if i == 19:
            if (floor_grid[i-1] != 1 and floor_grid[i-5] == 1):
                borders = rb.RoomBorders()
                return borders.down_door(p.BLUE)
                
            elif (floor_grid[i-1] != 1 or floor_grid[i-1] != 0 and
                    floor_grid[i-5] != 1 or floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.left_down_door(p.BLUE)
                
            elif (floor_grid[i-1] != 0 and floor_grid[i-5] != 1):
                borders = rb.RoomBorders()
                return borders.left_door(p.BLUE)
                
            elif (floor_grid[i-1] != 1 and floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.down_door(p.BLUE)
            
        elif i == 15 or i == 16 or i == 17 or i == 18:
            if (floor_grid[i+1] == 1 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.right_down_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    (floor_grid[i-5] != 1 or floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.left_down_door(p.BLUE)
                
            elif (floor_grid[i+1] != 0 and floor_grid[i-1] != 0 and (floor_grid[i-5] != 1 or
                    floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.left_right_door(p.BLUE)
                
            elif (floor_grid[i+1] != 0 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    (floor_grid[i-5] != 1 or floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.right_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and floor_grid[i-1] != 0 and (floor_grid[i-5] != 1 or
                    floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.left_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.down_door(p.BLUE)
             
        else:
            if (floor_grid[i+1] != 0 and floor_grid[i-1] != 0 and floor_grid[i+5] != 0 and
                    floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.all_doors(p.BLUE)
                
            elif (floor_grid[i+1] != 0 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    (floor_grid[i+5] != 1 or floor_grid [i+5] != 0) and floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.right_down_door(p.BLUE)
                
            elif (floor_grid[i+1] != 0 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    floor_grid[i+5] != 0 and (floor_grid[i-5] != 1 or floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.right_up_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and floor_grid[i-1] != 0 and floor_grid[i+5] != 0 and
                    (floor_grid[i-5] != 1 or floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.left_up_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and floor_grid[i-1] != 0 and
                    (floor_grid[i+5] != 1 or floor_grid[i+5] != 0) and floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.left_down_door(p.BLUE)
                
            elif (floor_grid[i+1] != 0 and floor_grid[i-1] != 0 and floor_grid[i+5] != 0 and
                    (floor_grid[i-5] != 1 or floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.left_right_up_door(p.BLUE)
                
            elif (floor_grid[i+1] != 0 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    floor_grid[i+5] != 0 and floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.right_up_down_door(p.BLUE)
                
            elif (floor_grid[i+1] != 0 and floor_grid[i-1] != 0 and (floor_grid[i+5] != 1 or
                    floor_grid[i+5] != 0) and (floor_grid[i-5] != 1 or floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.left_right_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    floor_grid[i+5] != 0 and floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.up_down_door(p.BLUE)
                
            elif (floor_grid[i+1] != 0 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    (floor_grid[i+5] != 1 or floor_grid[i+5] != 0) and (floor_grid[i-5] != 1 or
                    floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.right_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and floor_grid[i-1] != 0 and (floor_grid[i+5] != 1 or
                    floor_grid[i+5] != 0) and (floor_grid[i-5] != 1 or floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.left_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    floor_grid[i+5] != 0 and (floor_grid[i-5] != 1 or floor_grid[i-5] != 0)):
                borders = rb.RoomBorders()
                return borders.up_door(p.BLUE)
                
            elif (floor_grid[i+1] != 1 and (floor_grid[i-1] != 1 or floor_grid[i-1] != 0) and
                    (floor_grid[i+5] != 1 or floor_grid[i+5] != 0) and floor_grid[i-5] != 0):
                borders = rb.RoomBorders()
                return borders.down_door(p.BLUE)
        
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
            
            

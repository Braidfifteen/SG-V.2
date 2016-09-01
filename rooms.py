import pygame as pg
import prepare as p
import roombuild as rb
import random

class Room():
    def __init__(self, game, player, borders, number):
        self.game = game
        self.player = player
        self.room_no = number
        self.power_up_list = pg.sprite.Group()
        self.bullet_list = pg.sprite.Group()
        self.enemy_list = pg.sprite.Group()
        self.wall_list = pg.sprite.LayeredDirty()
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
        self.room_no_list = self.get_room_no_list()
        self.game = game
        self.player = player
        
    def get_room_no_list(self):
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
    
    def floor_grid(self):
        grid_list = []
        for i in range(20):
            grid_list.append(i)
        return grid_list

    def make_rooms(self):
        floor_grid = self.floor_grid()
        room_no_list = self.room_no_list
        for i in range(len(floor_grid)):
            if floor_grid[i] in room_no_list:
                borders = self.make_borders(i, room_no_list)
                floor_grid[i] = Room(self.game, self.player, borders, i)
        return floor_grid
    
    def make_borders(self, i, rN):
        borders = rb.RoomBorders()
        if i == 19:
            if i-1 in rN and i-5 in rN:
                return borders.left_down_door(p.BLUE)
                
            elif i-1 in rN and i-5 not in rN:
                return borders.left_door(p.BLUE)
                
            elif i-1 not in rN and i-5 in rN:
                return borders.down_door(p.BLUE)
                
        elif i == 16 or i == 17 or i == 18:
            if i-1 in rN and i+1 in rN and i-5 in rN:
                return borders.left_down_right_door(p.BLUE)
                
            elif i-1 not in rN and i+1 in rN and i-5 in rN:
                return borders.right_down_door(p.BLUE)
                
            elif i-1 in rN and i+1 in rN and i-5 not in rN:
                return borders.left_right_door(p.BLUE)
                
            elif i-1 in rN and i+1 not in rN and i-5 in rN:
                return borders.left_down_door(p.BLUE)
                
            elif i-1 not in rN and i+1 not in rN and i-5 in rN:
                return borders.down_door(p.BLUE)
                
            elif i-1 not in rN and i-5 not in rN and i+1 in rN:
                return borders.right_door(p.BLUE)
                
            elif i-1 in rN and i+1 not in rN and i-5 not in rN:
                return borders.left_door(p.BLUE)
                
        elif i == 15:
            if i+1 in rN and i-5 in rN:
                return borders.right_down_door(p.BLUE)
                
            elif i+1 in rN and i-5 not in rN:
                return borders.right_door(p.BLUE)
                
            elif i+1 not in rN and i-5 in rN:
                return borders.down_door(p.BLUE)
                
        elif i == 14 or i == 9:
            if i+5 in rN and i-1 in rN and i-5 in rN:
                return borders.left_up_down_door(p.BLUE)
                
            elif i+5 not in rN and i-1 in rN and i-5 in rN:
                return borders.left_down_door(p.BLUE)
                
            elif i+5 in rN and i-1 not in rN and i-5 in rN:
                return borders.up_down_door(p.BLUE)
                
            elif i+5 in rN and i-1 in rN and i-5 not in rN:
                return borders.left_up_door(p.BLUE)
                
            elif i+5 not in rN and i-5 not in rN and i-1 in rN:
                return borders.left_door(p.BLUE)
                
            elif i+5 not in rN and i-1 not in rN and i-5 in rN:
                return borders.down_door(p.BLUE)
                
            elif i+5 in rN and i-1 not in rN and i-5 not in rN:
                return borders.up_door(p.BLUE)
                
        elif i == 13 or i == 12 or i == 11 or i == 8 or i == 7 or i == 6:
            if i+5 in rN and i+1 in rN and i-5 in rN and i-1 in rN:
                return borders.all_doors(p.BLUE)
                
            elif i+5 in rN and i-5 in rN and i-1 in rN and i+1 not in rN:
                return borders.left_up_door(p.BLUE)
                
            elif i+5 not in rN and i+1 not in rN and i-1 in rN and i-5 in rN:
                return borders.left_down_door(p.BLUE)
                
            elif i+5 not in rN and i+1 not in rN and i-1 not in rN and i-5 in rN:
                return borders.down_door(p.BLUE)
                
            elif i+5 in rN and i-5 in rN and i+1 not in rN and i-1 not in rN:
                return borders.up_down_door(p.BLUE)
                
            elif i+5 in rN and i-5 not in rN and i+1 not in rN and i-1 not in rN:
                return borders.up_door(p.BLUE)
                
            elif i+5 not in rN and i-5 not in rN and i+1 in rN and i-1 in rN:
                return borders.left_right_door(p.BLUE)
                
            elif i+5 not in rN and i-5 not in rN and i+1 not in rN and i-1 in rN:
                return borders.left_door(p.BLUE)
                
            elif i+5 not in rN and i-5 not in rN and i-1 not in rN and i+1 in rN:
                return borders.right_door(p.BLUE)
                
            elif i+5 not in rN and i-5 in rN and i+1 in rN and i-1 in rN:
                return borders.left_down_right_door(p.BLUE)
                
            elif i+5 in rN and i+1 in rN and i-5 in rN and i-1 not in rN:
                return borders.right_up_down_door(p.BLUE)
                
            elif i+5 in rN and i+1 in rN and i-1 in rN and i-5 not in rN:
                return borders.left_up_right_door(p.BLUE)
                
            elif i+5 not in rN and i-1 not in rN and i+1 in rN and i-5 in rN:
                return borders.right_down_door(p.BLUE)
                
            elif i+5 in rN and i+1 in rN and i-5 not in rN and i-1 not in rN:
                return borders.right_up_door(p.BLUE)
                
            elif i+5 in rN and i-1 in rN and i+1 not in rN and i-5 not in rN:
                return borders.left_up_door(p.BLUE)
            
        elif i == 10 or i == 5:
            if i+5 in rN and i+1 in rN and i-5 in rN:
                return borders.right_up_down_door(p.BLUE)
                
            elif i+5 not in rN and i+1 in rN and i-5 in rN:
                return borders.right_down_door(p.BLUE)
                
            elif i+5 in rN and i+1 not in rN and i-5 in rN:
                return borders.up_down_door(p.BLUE)
                
            elif i+5 in rN and i+1 in rN and i-5 not in rN:
                return borders.right_up_door(p.BLUE)
                
            elif i+5 not in rN and i-5 not in rN and i+1 in rN:
                return borders.right_door(p.BLUE)
                
            elif i+5 not in rN and i+1 not in rN and i-5 in rN:
                return borders.down_door(p.BLUE)
                
            elif i+5 in rN and i+1 not in rN and i-5 not in rN:
                return borders.up_door(p.BLUE)
                
        elif i == 1 or i == 2 or i == 3:
            if i+5 in rN and i+1 in rN and i-1 in rN:
                return borders.left_up_right_door(p.BLUE)
                
            elif i+5 in rN and i+1 in rN and i-1 not in rN:
                return borders.right_up_door(p.BLUE)
                
            elif i+5 not in rN and i+1 in rN and i-1 in rN:
                return borders.left_right_door(p.BLUE)
                
            elif i+5 in rN and i+1 not in rN and i-1 in rN:
                return borders.left_up_door(p.BLUE)
                
            elif i+5 in rN and i+1 not in rN and i-1 not in rN:
                return borders.up_door(p.BLUE)
                
            elif i+5 not in rN and i-1 not in rN and i+1 in rN:
                return borders.right_door(p.BLUE)
                
            elif i+5 not in rN and i-1 in rN and i+1 not in rN:
                return borders.left_door(p.BLUE)
                
        elif i == 4:
            if i+5 in rN and i-1 in rN:
                return borders.left_up_door(p.BLUE)
                
            elif i+5 in rN and i-1 not in rN:
                return borders.up_door(p.BLUE)
                
            elif i+5 not in rN and i-1 in rN:
                return borders.left_door(p.BLUE)
                
        elif i == 0:
            if i+5 in rN and i+1 in rN:
                return borders.right_up_door(p.BLUE)
                
            elif i+5 not in rN and i+1 in rN:
                return borders.right_door(p.BLUE)
                
            elif i+5 in rN and i+1 not in rN:
                return borders.up_door(p.BLUE)
                
            
                
                
                
                
                
        
                
            
            

        
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
            
            

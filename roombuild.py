import pygame as pg
import prepare as p

class Wall(pg.sprite.DirtySprite):
    def __init__(self, room, game, x, y, width, height, color):
        self.groups = room.wall_list
        super().__init__(self.groups)
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dirty = 1
        
class RoomDoors():
    def __init__(self):
        pass
        
    def left_door(self, color):
        door = [[20, 450, 10, 100, color]]
        return door
        
    def right_door(self, color):
        door = [[1890, 450, 10, 100, color]]
        return door
        
    def top_door(self, color):
        door = [[900, 20, 100, 10, color]]
        return door
        
    def bottom_door(self, color):
        door = [[900, 1050, 100, 10, color]]
        return door
        
class RoomBorders():
    def __init__(self):
        pass
    
    def right_door(self, color):
                                # Top        
        border_list = [[0, 0, p.SCREEN_X, 30, color],
                        # Right-top
                       [1890, 0, 30, 450, color],
                        # Right-bottom
                       [1890, 550, 30, p.SCREEN_Y, color],
                       # Bottom
                       [0, 1050, p.SCREEN_X, 30, color],
                        # Left
                       [0, 0, 30, p.SCREEN_Y, color]
                      ]
        return border_list

    def left_door(self, color):
        
                               # Left-top
        border_list = [[0, 0, 30, 450, color],
                       # Left-bottom
                       [0, 550, 30, p.SCREEN_Y, color],
                       # Bottom
                       [0, 1050, p.SCREEN_X, 30, color],
                        # Right
                       [1890, 0, 30, p.SCREEN_Y, color],
                       # Top
                       [0, 0, p.SCREEN_X, 30, color]
                      ]
        return border_list      

    def up_door(self, color):
        
                        # Top-left
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Bottom
                       [0, 1050, p.SCREEN_X, 30, color],
                        # Right
                       [1890, 0, 30, p.SCREEN_Y, color],
                        # Left
                       [0, 0, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def down_door(self, color):
        
                                # Top
        border_list = [[0, 0, p.SCREEN_X, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Left
                       [0, 0, 30, p.SCREEN_Y, color],
                        # Right
                       [1890, 0, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
        
        
    def left_right_door(self, color):
        
                               # Left-top
        border_list = [[0, 0, 30, 450, color],
                       # Left-bottom
                       [0, 550, 30, p.SCREEN_Y, color],
                       # Bottom
                       [0, 1050, p.SCREEN_X, 30, color],
                       # Right-top
                       [1890, 0, 30, 450, color],
                       # Right-bottom
                       [1890, 550, 30, p.SCREEN_Y, color],
                       # Top
                       [0, 0, p.SCREEN_X, 30, color]
                      ]
        return border_list
    
    def up_down_door(self, color):
        
                                # Top-left
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Left
                       [0, 0, 30, p.SCREEN_Y, color],
                        # Right
                       [1890, 0, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def all_doors(self, color):
        border_list = [[0, 0, 900, 30, color],
                       [1000, 0, 920, 30, color],
                       [0, 1050, 900, 30, color],
                       [1000, 1050, 920, 30, color],
                       [0, 0, 30, 450, color],
                       [0, 550, 30, p.SCREEN_Y, color],
                       [1890, 0, 30, 450, color],
                       [1890, 550, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def left_up_door(self, color):
        
                                # Top-left
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Bottom
                       [0, 1050, p.SCREEN_X, 30, color],
                        # Right
                       [1890, 0, 30, p.SCREEN_Y, color],
                        # Left-top
                       [0, 0, 30, 450, color],
                        # Left-bottom
                       [0, 550, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def right_up_down_door(self, color):
        
                        # Top-left
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Left
                       [0, 0, 30, p.SCREEN_Y, color],
                       # Right-top
                       [1890, 0, 30, 450, color],
                       # Right-bottom
                       [1890, 550, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def left_up_down_door(self, color):
        
                                # Top-left
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Bottom_right
                       [1000, 1050, 920, 30, color],
                        # Right
                       [1890, 0, 30, p.SCREEN_Y, color],
                        # Left-top
                       [0, 0, 30, 450, color],
                        # Left-bottom
                       [0, 550, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def left_up_right_door(self, color):
        
                                # Top-left
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Bottom
                       [0, 1050, p.SCREEN_X, 30, color],
                       # Right-top
                       [1890, 0, 30, 450, color],
                       # Right-bottom
                       [1890, 550, 30, p.SCREEN_Y, color],
                        # Left-top
                       [0, 0, 30, 450, color],
                        # Left-bottom
                       [0, 550, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def left_down_door(self, color):
        
                                # Top
        border_list = [[0, 0, p.SCREEN_X, 30, color],
                        # Right
                       [1890, 0, 30, p.SCREEN_Y, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Left-bottom
                       [0, 550, 30, p.SCREEN_Y, color],
                        # Left-top
                       [0, 0, 30, 450, color]
                      ]
        return border_list      
        
    def left_down_right_door(self, color):
        
                        # Top
        border_list = [[0, 0, p.SCREEN_X, 30, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                       # Right-top
                       [1890, 0, 30, 450, color],
                       # Right-bottom
                       [1890, 550, 30, p.SCREEN_Y, color],
                        # Left-top
                       [0, 0, 30, 450, color],
                        # Left-bottom
                       [0, 550, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def right_down_door(self, color):
        
                                # Top        
        border_list = [[0, 0, p.SCREEN_X, 30, color],
                        # Right-top
                       [1890, 0, 30, 450, color],
                        # Right-bottom
                       [1890, 550, 30, p.SCREEN_Y, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Left
                       [0, 0, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
    def right_up_door(self, color):
        
                                # Top-left       
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Right-top
                       [1890, 0, 30, 450, color],
                        # Right-bottom
                       [1890, 550, 30, p.SCREEN_Y, color],
                        # Bottom
                       [0, 1050, p.SCREEN_X, 30, color],
                        # Left
                       [0, 0, 30, p.SCREEN_Y, color]
                      ]
        return border_list
        
        
        
        
        
        
        
        
        
        
        
        
        
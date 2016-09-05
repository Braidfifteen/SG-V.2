import pygame as pg
import prepare as p

class Player(pg.sprite.DirtySprite):
    """Class that creates the sprite the user will control."""
    def __init__(self, game, x, y, color, width, height):
        self.groups = game.all_sprites
        super().__init__(self.groups)
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = x
        self.rect.y = y
        self.moveX = 0
        self.moveY = 0
        self.health = 100
        self.room = None
        self.health_timer = 0
        self.health_cooldown = 400
        self.damage = 10
        self.speed = 6
        self.shot_timer = 0
        self.shot_cooldown = 100
        self.is_shooting = False
        self.logic = PlayerLogic(self)
        self.room_change = RoomChange(self, game)
        self.dirty = 1
        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_right = False
        self.is_moving_left = False

    def move_right(self):
        self.moveX = self.speed

    def move_left(self):
        self.moveX = -self.speed
        
    def move_up(self):
        self.moveY = -self.speed
        
    def move_down(self):
        self.moveY = self.speed
        
    def stopY(self):
        self.moveY = 0
        
    def stopX(self):
        self.moveX = 0
        
    def get_event(self, event):
        """Handles all events that pertains to playable character."""

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                print(self.game.current_room_no)
            if event.key == pg.K_BACKSPACE:
                print(self.game.room.room_no_list)
            if event.key == pg.K_a:
                self.is_moving_left = True                
                self.move_left()
            if event.key == pg.K_d:
                self.is_moving_right = True                
                self.move_right()
            if event.key == pg.K_w:
                self.is_moving_up = True
                self.move_up()                
            if event.key == pg.K_s:
                self.is_moving_down = True
                self.move_down()                
        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                if self.is_moving_right == True:
                    self.is_moving_left = False                    
                    self.move_right()
                else:
                    self.is_moving_left = False                    
                    self.stopX()
            if event.key == pg.K_d:
                if self.is_moving_left == True:
                    self.is_moving_right = False
                    self.move_left()                    
                else:
                    self.is_moving_right = False                    
                    self.stopX()
            if event.key == pg.K_w:
                if self.is_moving_down == True:
                    self.is_moving_up = False                    
                    self.move_down()
                else:
                    self.is_moving_up = False                    
                    self.stopY()
            if event.key == pg.K_s:
                if self.is_moving_up == True:
                    self.is_moving_down = False                    
                    self.move_up()
                else:
                    self.is_moving_down = False                    
                    self.stopY()

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.is_shooting = True
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.is_shooting = False
            
    def update(self):
        """Update image and position of sprite."""
        if self.is_moving_up:
            self.dirty = 1
        if self.is_moving_down:
            self.dirty = 1
        if self.is_moving_right:
            self.dirty = 1
        if self.is_moving_left:
            self.dirty = 1
        
        self.rect.x += self.moveX
        self.logic.wall_hit_logic(self.moveX, "x", self.room.wall_list)
        self.room_change.change_room()
        
        self.rect.y += self.moveY
        self.logic.wall_hit_logic(self.moveY, "y", self.room.wall_list)
        self.room_change.change_room()
        
class PlayerLogic():
    def __init__(self, player, items=None):
        self.player = player

        
    def wall_hit_logic(self, move, direction, items):
        if direction == "x":
            wall_hit_list = pg.sprite.spritecollide(self.player, items, False)
            for wall in wall_hit_list:
                if move > 0:
                    self.player.rect.right = wall.rect.left
                else:
                    self.player.rect.left = wall.rect.right
        elif direction == "y":
            wall_hit_list = pg.sprite.spritecollide(self.player, items, False)
            for wall in wall_hit_list:
                if move > 0:
                    self.player.rect.bottom = wall.rect.top
                else:
                    self.player.rect.top = wall.rect.bottom
                    
class RoomChange():
    def __init__(self, player, game):
        self.player = player
        self.game = game
        
    def change_room(self):
        if self.game.current_room_no == 0:
            if self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 1
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 5
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 1:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 0
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 2
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 6
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 2:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 1
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 3
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 7
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 3:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 2
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 4
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 8
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 4:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 3
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 9
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 5:
            if self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 6
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 10
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 0
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 6:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 5
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 7
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 11
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 1
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
                
        elif self.game.current_room_no == 7:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 6
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 8
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 12
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 2
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 8:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 7
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 9
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 13
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 3
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 9:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 8
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 14
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 4
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 10:
            if self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 11
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 15
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 5
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 11:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 10
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 12
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 16
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 6
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 12:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 11
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 13
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 17
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 7
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 13:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 12
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 14
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 18
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 8
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 14:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 13
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y <= -30:
                self.game.current_room_no = 19
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = p.SCREEN_Y - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 9
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 15:
            if self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 16
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 10
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 16:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 15
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 17
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 11
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 17:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 16
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 18
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 12
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 18:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 17
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.x >= p.SCREEN_X:
                self.game.current_room_no = 19
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 13
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                
        elif self.game.current_room_no == 19:
            if self.player.rect.x <= -15:
                self.game.current_room_no = 18
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.x = p.SCREEN_X - 30
                self.player.room = self.game.current_room
            elif self.player.rect.y >= p.SCREEN_Y:
                self.game.current_room_no = 14
                self.game.current_room = self.game.room_list[self.game.current_room_no]
                self.player.rect.y = 30
                self.player.room = self.game.current_room
                

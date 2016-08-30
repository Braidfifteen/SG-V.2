import pygame as pg
import prepare as p

class Player(pg.sprite.Sprite):
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
            if event.key == pg.K_a:
                self.move_left()
            if event.key == pg.K_d:
                self.move_right()
            if event.key == pg.K_w:
                self.move_up()
            if event.key == pg.K_s:
                self.move_down()
        if event.type == pg.KEYUP:
            if event.key == pg.K_a and self.moveX < 0:
                self.stopX()
            if event.key == pg.K_d and self.moveX > 0:
                self.stopX()
            if event.key == pg.K_w and self.moveY < 0:
                self.stopY()
            if event.key == pg.K_s and self.moveY > 0:
                self.stopY()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.is_shooting = True
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.is_shooting = False
            
    def update(self):
        """Update image and position of sprite."""
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
        if self.player.rect.x >= p.SCREEN_X:
            self.game.current_room_no += 1
            self.game.current_room = self.game.room_list[self.game.current_room_no]
            self.player.rect.x = 30
            self.player.room = self.game.current_room
        elif self.player.rect.x <= 0:
            self.game.current_room_no -= 1
            self.game.current_room = self.game.room_list[self.game.current_room_no]
            self.player.rect.x = p.SCREEN_X - 30
            self.player.room = self.game.current_room
        elif self.player.rect.y <= -15:
            self.game.current_room_no += 5
            self.game.current_room = self.game.room_list[self.game.current_room_no]
            self.player.rect.y = p.SCREEN_Y
            self.player.room = self.game.current_room
        elif self.player.rect.y >= p.SCREEN_Y:
            self.game.current_room_no -= 5
            self.game.urrent_room = self.game.room_list[self.game.current_room_no]
            self.player.rect.y = 15
            self.player.room = self.game.current_room
    """
    def change_room(self, current_no):
        if self.current_room_no == 0:
            if self.player.rect.x >= p.SCREEN_W:
                self.current_room_no = 1
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.current_room
            elif player.rect.y <= -30:
                self.current_room_no = 5
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.y = SCREEN_H + 30
                self.player.room = self.current_room
                
        elif self.current_room_no == 1:
            if player.rect.x <= -15:
                self.current_room_no = 0
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.x = SCREEN_W
                self.player.room = self.current_room
            elif player.rect.x >= SCREEN_W:
                self.current_room_no = 2
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.current_room
            elif player.rect.y <= -30:
                self.current_room_no = 6
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.y = SCREEN_H + 30
                self.player.room = self.current_room
                
        elif self.current_room_no == 2:
            if player.rect.x <= -15:
                self.current_room_no = 1
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.x = SCREEN_W
                self.player.room = self.current_room
            elif player.rect.x >= SCREEN_W:
                self.current_room_no = 3
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.current_room
            elif self.player.rect.y <= -30:
                self.current_room_no = 7
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.y = SCREEN_H + 30
                self.player.room = self.current_room
                
        elif self.current_room_no == 3:
            if player.rect.x <= -15:
                self.current_room_no = 2
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.x = SCREEN_W
                self.player.room = self.current_room
            elif player.rect.x >= SCREEN_W:
                self.current_room_no = 4
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.x = 30
                self.player.room = self.current_room
            elif self.player.rect.y <= -30:
                self.current_room_no = 8
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.y = SCREEN_H + 30
                self.player.room = self.current_room
                
        elif self.current_room_no == 4:
            if player.rect.x <= -15:
                self.current_room_no = 3
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.x = SCREEN_W
                self.plyaer.room = self.current_room
            elif player.rect.y <= -30:
                self.current_room_no = 9
                self.current_room = self.room_list[self.current_room_no]
                self.player.rect.y = SCREEN_H + 30
                self.player.room = self.current_room
                """
        
            
        
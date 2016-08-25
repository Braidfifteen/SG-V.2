import pygame as pg
import prepare

class Sprite(pg.sprite.Sprite):
    """Basic sprite class for all sprites."""
    def __init__(self, x, y, color, width, height, *groups):
        super().__init__(x, y, color, width, height, *groups)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(Sprite):
    """Class that creates the sprite the user will control."""
    def __init__(self, x, y, color, width, height, *groups):
        super().__init__(x, y, color, width, height, *groups)
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
        
    def move_right(self):
        self.moveX = self.speed
        
    def move_left(self):
        self.moveX = -self.speed
        
    def move_up(self):
        self.moveY = -self.speed
        
    def move_down(self):
        self.moveY = self.speed
        
    def get_event(self, event):
        """Handles all events that pertains to playable character."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_left()
            if event.key == pygame.K_d:
                player.move_right()
            if event.key == pygame.K_w:
                player.move_up()
            if event.key == pygame.K_s:
                player.move_down()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.moveX < 0:
                player.stopX()
            if event.key == pygame.K_d and player.moveX > 0:
                player.stopX()
            if event.key == pygame.K_w and player.moveY < 0:
                player.stopY()
            if event.key == pygame.K_s and player.moveY > 0:
                player.stopY()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.is_shooting = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                player.is_shooting = False
        
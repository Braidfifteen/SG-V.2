import sys
import pygame as pg
import prepare


class App():
    """Main class that runs the program."""
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.app_running = True
        self.clock = pg.time.Clock()
        self.player = None
        
    def event_loop(self):
        """
        Processes all events.
        Sends events to player so they can also process events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.app_running = False
            self.player.get_event(event)
                
                
        
        

import sys
import pygame as pg
import prepare
import sprites


class App():
    """Main class that runs the program."""
    def __init__(self):
        self.screen = pg.Surface(prepare.WINDOW.get_size())
        self.screen.fill(prepare.WHITE)
        prepare.WINDOW.blit(self.screen, [0,0])
        self.screen_rect = self.screen.get_rect()
        self.app_running = True
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.RenderUpdates()
        self.player = sprites.Player(50, 50, prepare.BLUE, 20, 20)
        self.player.add(self.all_sprites)
        pg.display.update()


        
        
        
    def event_loop(self):
        """
        Processes all events.
        Sends events to player so they can also process events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.app_running = False
            self.player.get_event(event)
            
    def display_fps(self):
        """Show FPS in the program window."""
        template = "{} - FPS: {:.2f}"
        caption = template.format(prepare.CAPTION, self.clock.get_fps())
        pg.display.set_caption(caption)
        
    def update(self):
        """Update all sprites."""
        self.all_sprites.clear(prepare.WINDOW, self.screen)
        self.all_sprites.update()
        
    def render(self):
        """Clear screen and render all sprites to screen."""
        
        dirty = self.all_sprites.draw(prepare.WINDOW)
        pg.display.update(dirty)
        
    def main_loop(self):
        """
        The main game loop.
        Process events; update; render.
        """
        while self.app_running:
            self.event_loop()
            self.update()
            self.render()
            self.clock.tick(prepare.FPS)
            self.display_fps()
                
                
def main():
    """Create an App and start the program."""
    App().main_loop()
    pg.quit()
    sys.exit()
    
    
if __name__ == "__main__":
    main()
import sys
import game
import pygame as pg

def main():
    """Create an App and start the program."""
    game.App().new()
    pg.quit()
    sys.exit()
     
if __name__ == "__main__":
    main()
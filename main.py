import sys
import app as a
import pygame as pg

def main():
    """Create an App and start the program."""
    a.App().new()
    pg.quit()
    sys.exit()
     
if __name__ == "__main__":
    main()
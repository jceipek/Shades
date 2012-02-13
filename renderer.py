import pygame
import math

from settings import Settings
from engine.functions import pathJoin

class CustomRenderer:
    
    def __init__(self, imageCache=None):
        self.avatar = None
        CustomRenderer.imageCache = imageCache
        pygame.init()
        self.display = pygame.display.set_mode((Settings.SCREEN_WIDTH,
                                          Settings.SCREEN_HEIGHT))
        pygame.display.set_caption("Shades")

    def addAvatar(self, avatar):
        self.avatar = avatar
        
    def render(self, clock=None):
        self.display.fill((0,0,0))
        pygame.draw.rect(self.display, (255,0,0), pygame.Rect(self.avatar.getBounds()))
        if clock:
            pygame.display.set_caption("Shades Demo at fps: "+str(clock.get_fps()))
        pygame.display.flip()
         

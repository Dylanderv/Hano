# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
from class_Animated import *

#Atk Effect est le spell en lui meme
#Carastéristiques des atk effect:
#   un set d'images (pas d'état)
#   des dégâts (dmg)
#   une force de répulsion px/fps(knockback)
#   une durée ms(duration) => l'attaque disparait au contact de toute façon
#   un poids acc_y(weight)
#   une vitesse initiale px/fps (speed_x et speed_y)
class AtkEffect(Animated):
    def __init__(self, x, y, width, height, images, dmg , knockback, weight, speed_x, speed_y, duration):
        Animated.__init__(self, x, y, width, height)
        self.dmg = dmg
        self.knockback = knockback
        self.projection = projection
        self.duration = duration
        self.images = images

    def update(self, fps):
        if(self.duration > 0):
            self.duration = self.duration - (1000/fps)
            self.speed_y += self.weight
            self.x += self.speed_x
            self.y += self.speed_y
            Animated.update(self)
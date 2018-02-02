import pygame
from pygame.locals import *
pygame.init()
events=[]
def keyheld(key) :
    return pygame.key.get_pressed()[key]
def keydown(key) :
    for event in events :
        if event.type == pygame.KEYDOWN and event.key == key :
            return True
    return False
def keyup(key) :
    for event in events :
        if event.type == pygame.KEYUP and event.key == key :
            return True
    return False
def modkeys() :
    keys=pygame.key.get_pressed()
    mods={K_LALT:False,K_RALT:False,K_LCTRL:False,K_RCTRL:False,K_LSHIFT:False,K_RSHIFT:False,K_LMETA:False,K_RMETA:False}
    for modkey in mods.keys() :
        if keys[modkey] :
            mods[modkey]=True
    return mods
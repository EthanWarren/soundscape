#The module responsible for the playing and panning of sounds.
#Only supports right and left panning at the moment.

import pygame,os
pygame.init()
pygame.mixer.set_num_channels(10000)
sounds=[]
class PositionedSound() :
    def __init__(self,file) :
        sounds.append(self)
        self.sound=pygame.mixer.Sound(file)
        self.channel=pygame.mixer.find_channel()
        self.channel.play(self.sound,loops=-1)
        self.channel.set_volume(0.0,0.0)
        self.volume=[0.0,0.0]
        self.pos=-11
    def set_position(self,pos) :
        volumes={-10:[0.1,0.0],-9:[0.2,0.0],-8:[0.3,0.0],-7:[0.4,0.0],-6:[0.5,0.0],-5:[0.6,0.0],-4:[0.7,0.0],-3:[0.8,0.0],-2:[0.9,0.0],-1:[1,0],0:[1,1],1:[0,1],2:[0,0.9],3:[0,0.8],4:[0,0.7],5:[0,0.6],6:[0,0.5],7:[0,0.4],8:[0,0.3],9:[0,0.2],10:[0,0.1],-11:[0.0,0.0],11:[0.0,0.0]}
        if pos in range(-11,12) :
            self.volume=volumes[pos]
            self.pos=pos
        else :
            self.volume=volumes[-11]
            self.pos=-11
    def get_position(self) :
        return self.pos
    def update(self) :
        self.channel.set_volume(self.volume[0],self.volume[1])
class Sound() :
    def __init__(self,file) :
        self.sound=pygame.mixer.Sound(file)
    def play(self,position=0) :
        volumes={-10:[0.1,0.0],-9:[0.2,0.0],-8:[0.3,0.0],-7:[0.4,0.0],-6:[0.5,0.0],-5:[0.6,0.0],-4:[0.7,0.0],-3:[0.8,0.0],-2:[0.9,0.0],-1:[1,0],0:[1,1],1:[0,1],2:[0,0.9],3:[0,0.8],4:[0,0.7],5:[0,0.6],6:[0,0.5],7:[0,0.4],8:[0,0.3],9:[0,0.2],10:[0,0.1],-11:[0.0,0.0],11:[0.0,0.0]}
        if position in range(-10,11) :
            c=self.sound.play()
            c.set_volume(volumes[position][0],volumes[position][1])
    def pause(self) :
        self.sound.pause()
    def stop(self) :
        self.sound.stop()
def set_background_music(file) :
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
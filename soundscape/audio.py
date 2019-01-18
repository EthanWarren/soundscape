#The module responsible for the playing and panning of sounds.

import pygame,os
from openal.audio import SoundSink,SoundSource
from openal.loaders import load_wav_file
pygame.init()
sink=SoundSink()
sink.activate()
class PositionedSound() :
    def __init__(self,file,position=(1000000,1000000,1000000)) :
        self.source=SoundSource(position=position)
        self.source.looping=True
        self.data=load_wav_file(file)
        self.source.queue(self.data)
        sink.play(self.source)
    def silence(self) :
        self.set_position((1000000,1000000,1000000))
    def set_position(self,position) :
        self.source.position=position
    def get_position(self) :
        return self.source.position
class Sound() :
    def __init__(self,file) :
        self.data=load_wav_file(file)
    def play(self,position=(0,0,0)) :
        source=SoundSource(position=position)
        source.looping=False
        source.queue(self.data)
        sink.play(self.source)
def set_background_music(file) :
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
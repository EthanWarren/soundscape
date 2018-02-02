#Main app class.
#Run it's update method every iteration of the loop to deal with display functions out of audio concerns.

import pygame,speech,audio,keyboard,sys
pygame.init()
class App() :
    def __init__(self,name,startprompt="") :
        self.screen=pygame.display.set_mode((1000,1000))
        self.clock=pygame.time.Clock()
        pygame.display.set_caption(name)
        speech.say(startprompt)
    def update(self,color=(0,0,0),fps=30) :
        keyboard.events=pygame.event.get()
        for sound in audio.sounds :
            sound.update()
        self.screen.fill(color)
        pygame.display.update()
        self.clock.tick(fps)
    def quit(self) :
        pygame.quit()
        sys.exit()
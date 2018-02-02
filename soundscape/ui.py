import pygame,speech
pygame.init()
class Textbox() :
    def __init__(self,prompt) :
        self.prompt=prompt
        self.screen=pygame.display.set_mode((1000,1000))
    def run(self) :
        result=""
        speech.say(self.prompt)
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE :
                    speech.charsay(event.unicode)
                    result=result+event.unicode
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE :
                    result=result[:-1]
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN :
                    return result
            self.screen.fill((0,0,0))
            pygame.display.update()
class Menu() :
    def __init__(self,options,scrollsound=None,clicksound=None,boundarysound=None,downkey=pygame.K_DOWN,upkey=pygame.K_UP,clickkey=pygame.K_RETURN,startprompt="") :
        speech.say(startprompt)
        self.options=options
        self.pos=0
        self.clicksound=clicksound
        self.scrollsound=scrollsound
        self.boundarysound=boundarysound
        self.downkey=downkey
        self.upkey=upkey
        self.clickkey=clickkey
        self.screen=pygame.display.set_mode((1000,1000))
    def run(self) :
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN and event.key == self.downkey :
                    if self.pos < len(self.options)-1 :
                        self.pos+=1
                        if self.scrollsound is not None :
                            self.scrollsound.play()
                        speech.say(self.options[self.pos][0])
                    else :
                        if self.boundarysound is not None :
                            self.boundarysound.play()
                if event.type == pygame.KEYDOWN and event.key == self.upkey :
                    if self.pos > 0 :
                        self.pos-=1
                        if self.scrollsound is not None :
                            self.scrollsound.play()
                        speech.say(self.options[self.pos][0])
                    else :
                        if self.boundarysound is not None :
                            self.boundarysound.play()
                if event.type == pygame.KEYDOWN and event.key == self.clickkey :
                    if self.clicksound is not None :
                        self.clicksound.play()
                    self.options[self.pos][1]()
                    return None
            self.screen.fill((0,0,0))
            pygame.display.update()
"""This module contains the main app class."""

import pygame,speech,audio,keyboard,sys
pygame.init()
class App() :
    """This is the main app class.
soundscape.app.App(name,startprompt="") > soundscape.app.App object
The name is the caption for the audio game's window and the startprompt is a speech introduction to the game."""
    def __init__(self,name,startprompt="") :
        self.screen=pygame.display.set_mode((1000,1000))
        self.clock=pygame.time.Clock()
        pygame.display.set_caption(name)
        speech.say(startprompt)
    def update(self,color=(0,0,0),fps=30) :
        """soundscape.app.App.update(color=(0,0,0),fps=30) > None
The color is a pygame style rgb value and fps is the maximum frame rate.
Since this is an audio game library, most of the time these values can remain unchanged.
Call this method at the top of the main loop to update the display and audio player."""
        keyboard.events=pygame.event.get()
        audio.sink.update()
        self.screen.fill(color)
        pygame.display.update()
        self.clock.tick(fps)
    def quit(self) :
        """soundscape.app.App.quit() > none
This method quits the application.
Use it when you need to exit."""
        pygame.quit()
        sys.exit()
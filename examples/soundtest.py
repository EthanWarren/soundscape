import soundscape
app=soundscape.app.App("test")
x=0
y=0
z=0
s=soundscape.audio.PositionedSound("a.wav",position=(x,y,z))
while True :
    app.update()
    if soundscape.keyboard.keydown(soundscape.K_q) :
        app.quit()
    if soundscape.keyboard.keydown(soundscape.K_RIGHT) :
        x+=2
    if soundscape.keyboard.keydown(soundscape.K_LEFT) :
        x-=2
    if soundscape.keyboard.keydown(soundscape.K_UP) :
        z-=2
    if soundscape.keyboard.keydown(soundscape.K_DOWN) :
        z+=2
    if soundscape.keyboard.keydown(soundscape.K_s) :
        y-=2
    if soundscape.keyboard.keydown(soundscape.K_w) :
        y+=2
    s.set_position((x,y,z))
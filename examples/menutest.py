import soundscape
app=soundscape.app.App("test")
men=soundscape.ui.Menu(options=["talk","exit"],startprompt="main menu, talk")
while True :
    app.update()
    x=men.run()
    if x == 0 :
        soundscape.speech.say("hi")
    elif x == 1 :
        app.quit()
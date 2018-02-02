import os,platform
def say(txt) :
    OS=platform.system()
    if OS == "Windows" or OS == "Linux" :
        try :
            import espeak
            espeak.synth("{}".format(txt))
        except :
            print "Soundscape uses espeak for speech on linux and windows, please install it before using it on thOSe platforms."
    elif OS == "Darwin" :
        os.system("say \"{}\" &".format(txt))
    else :
        print "Speech is not currently supported on your platform."
def charsay(char) :
    if char == " " :
        say("space")
    elif char.isupper() :
        say("cap {}".format(char))
    elif char == "." :
        say("period")
    elif char == "!" :
        say("exclaim")
    elif char == "?" :
        say("question")
    elif char == ";" :
        say("semicolen")
    elif char == ":" :
        say("colen")
    elif char == "/" :
        say("slash")
    elif char == "\\" :
        say("backslash")
    elif char == "^" :
        say("carrot")
    elif char == "[" :
        say("left bracket")
    elif char == "]" :
        say("right bracket")
    elif char == "{" :
        say("left brace")
    elif char == "}" :
        say("right brace")
    elif char == "(" :
        say("left paren")
    elif char == ")" :
        say("right paren")
    elif char == "|" :
        say("virticle line")
    elif char == "_" :
        say("underscore")
    elif char == "-" :
        say("dash")
    elif char == "," :
        say("comma")
    else :
       say(char)
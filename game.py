import pygame
from pygame.locals import *
import secrets 
import random
import os


data = {
"0": ["a","a","ba","ca","ba"],
"1": ["da","ca","ba","da","sa","sa"],
"2": ["ma","sa","ya","ma","ya","ma"],
"3": ["i","ba","bi","ca","ci","da"],
"4": ["mi","ya","yi","di","sa","si"],
"5": ["da","yi","si","bi","sa","di"],
"6": ["a","ci","ca","di","ma","ya"],
"7": ["u","bu","cu","du","mu","yu"],
"8": ["du","cu","su","bu","ci","da"],
"9": ["ni","na","nu","ni","ba","nu"],
"10": ["di","si","ni","ma","ni","da"],
"11": ["ka","ki","ku","suka","kaki","kuku"],
"12": ["pi","pa","pu","pipa","ku","kupu"],
"13": ["li","la","lu","bali","bulu","la"],
"14": ["ta","ti","tu","ta","bata","tati"],
"15": ["batu","ra","ri","ru","bara","duri"],
"16": ["ra","ri","ru","bara","baru","duri"],
"17": ["hi","ha","hu","paha","dahi","bahu"],
"18": ["ka","si","sa","ma","ta","ga","na"]
}

level = 18
toread = []
pos = 0

def builddata(n):
    rslt = []
    for i in range(n):
        rslt.extend(data[str(i)])
    return rslt


def formdata():
    global toread, level
    data = builddata(level)
    rst = []
    for i in range(6):
        rst.append(secrets.choice(data))
    print('rst:',rst)
    toread = rst


def buildseq():
    global pos
    rslt = ""    
    bold = ""
    for idx,i in enumerate(toread):
        if idx != pos:
            if len(i) == 2:
                rslt = rslt + str(i) + " "
                bold = bold + "   "
            if len(i) == 4:
                rslt = rslt + str(i) + " "
                bold = bold + "     "               
        else:
            if len(i) == 2:
                rslt = rslt + "   "
                bold = bold + str(i) + " "
            if len(i) == 4:
                rslt = rslt + "     "
                bold = bold + str(i) + " "
                

    print('rslt',rslt)
    return rslt, bold

    

def color_for_index(i):
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def displaytext(screen):
    global pos, level
    global toread


    basicfont = pygame.font.Font("monos.ttf", 90)
    lvfont = pygame.font.Font("monos.ttf", 30)
    lv = lvfont.render(str(level), True, (0,0,0))

    images = []
    rslt , bold = buildseq()

    text = basicfont.render(rslt, True, (0,0,0))
    images.append(text)

    text = basicfont.render(bold, True, (255,0,0))
    images.append(text)

    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.fill((255, 255, 255))
    for i in images:
        screen.blit(i, textrect)
    texx = lv.get_rect()
    screen.blit(lv, texx)

    pygame.display.update()
    
    
def playsound(sound):
    pygame.mixer.Sound.play(sound)
    #pygame.mixer.music.stop()

def main():
    global pos, level, toread
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Baca Saya")
    screen = pygame.display.set_mode((1080,700))

    app1 = pygame.mixer.Sound("applause.wav")
    errowav = pygame.mixer.Sound("error.wav")
    errowav2 = pygame.mixer.Sound("error2.wav")

    formdata()

    # define a variable to control the main loop
    running = True
     
    clock = pygame.time.Clock()
    
    displaytext(screen)

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    pygame.display.iconify()

                if event.key == pygame.K_1:
                    pass

                if event.key == pygame.K_q:
                    print("Quitting")
                    pygame.quit()
                if event.key == pygame.K_DOWN:
                    playsound(errowav)
                    
                if event.key == pygame.K_RIGHT:
                    pos = pos + 1
                    displaytext(screen) 
                    if pos == 6:
                        pos = 0
                        formdata()
                        displaytext(screen)
                    
                if event.key == pygame.K_UP:
                    playsound(app1)
                    print("up")
                if event.key == pygame.K_LEFT:
                    pos = pos - 1
                    displaytext(screen)
                
                if event.key == pygame.K_a:
                    level = level+1
                    formdata()
                    displaytext(screen)

                if event.key == pygame.K_z:
                    level = level-1
                    formdata()
                    displaytext(screen)
                
                if event.key == pygame.K_SPACE:
                    pos = 0
                    formdata()
                    displaytext(screen)

                if event.key == pygame.K_DELETE:
                    playsound(errowav2)



def get_key_events():
    pass

if __name__=="__main__":
    # call the main function
    main()
def main():
import pygame,sys
import random
import math
from pygame.locals import*
from pygame import mixer

pygame.init()


#screen size
screen = pygame.display.set_mode((500,500))

#Bg img and Music
background = pygame.image.load('background1.jpg')
mixer.music.load('Battleground.wav')
mixer.music.play(-1)                                            #-1 is given for loop

#Title and Icon
pygame.display.set_caption("Corona")
icon = pygame.image.load('virus.png')
pygame.display.set_icon(icon)


#doctor
DoctorImg=pygame.image.load('doctor.png')
doctorX=220
doctorY=420
dx =0


#corona
CoronaImg = []
coronaX= []
coronaY= []
cx = []
cy = []
num_of_corona = 3

for i in range(num_of_corona):
    
    CoronaImg.append(pygame.image.load('corona.png'))
    coronaX.append(random.randint(0,435))
    coronaY.append(random.randint(50,80))
    cx .append(1.5)
    cy .append(40)


#injection
InjectionImg=pygame.image.load('injection1.png')
injectionX=0
injectionY=420
ix = 0
iy =4
injection_state = "ready"

#Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10


GameOverImg=pygame.image.load('gameoverE.jpg')


#defining esc key fn
def myquit():                                           
    pygame.quit()                                               
    sys.exit(0)                                                         


#defining doctor fn
def doctor(x,y):
    screen.blit(DoctorImg,(x,y))                                   #blit is used to draw


#defining corona fn
def corona(x, y, i):
    screen.blit(CoronaImg[i],(x,y))                                   #blit is used to draw


#defining injection fn
def fire_injection(x,y):
    global injection_state
    injection_state = "fire"
    screen.blit(InjectionImg,(x+1,y+1))


#defining collision fn
def iscollision(coronaX,coronaY,injectionX,injectionY):
    distance = math.sqrt(math.pow(coronaX - injectionX,2)) +(math.pow(coronaY - injectionY,2))
    if distance < 27:
        return True
    else:
        return False


#defining score fn
def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


#defining game over fn
def game_over_img():
    screen.blit(GameOverImg,(0,0))


#exit button an bg colour
def main():
    while True:
        screen.fill((169,169,169))                                                              #BGcolor
        screen.blit(background,(0,0))
        
                
        for event in pygame.event.get():                                                #X button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    #defining pressing keys
            if event.type == pygame.KEYDOWN:                                    #KEYDOWN is a fn denotes when a key is pressed


    #defining escape key
                if event.key==K_ESCAPE:
                     myquit()

                if event.key==K_F4:
                    myquit()


    #defining of LEFT key
                if event.key == pygame.K_LEFT:
                    dx = -3                                             #0.1 denoes the speed of the doctor
                   
                    
    #defining of RIGHT key
                if event.key == pygame.K_RIGHT:
                    dx = 3


    #defining of SPACE key
                if event.key == pygame.K_SPACE:
                    if injection_state=="ready":
                        injectionX=doctorX
                        fire_injection(injectionX,injectionY)
                    
                    

    #defining releasing keys
            if event.type == pygame.KEYUP:                                          #KEYUP is a fn denotes when a key is released

    #condition statement
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0


    #calling doctor
        doctorX += dx

    #doctor boundaries
        if doctorX <=0:
            doctorX=0
        elif doctorX >=436:
            doctorX=436


    #calling corona
        for i in range(num_of_corona):
            if coronaY[i] > 400:
                for j in range(num_of_corona):
                    coronaY[i] = 2000
                    game_over_img()
                    pass
                
            coronaX[i]+= cx[i]

    #corona boundaries
            if coronaX[i] <=0:
                cx[i]=1.5
                coronaY[i] +=cy[i]
            elif coronaX[i] >=436:
                cx[i]= -1.5
                coronaY[i] +=cy[i]


    #calling collision
            collision = iscollision(coronaX[i],coronaY[i],injectionX,injectionY)
            if collision:
                    collision_sound = mixer.Sound('attack.wav')
                    collision_sound.play()
                    injectionY = 420
                    injection_state = "ready"
                    score_value  +=1
                    coronaX[i]=random.randint(0,435)
                    coronaY[i]=random.randint(50,80)
            corona(coronaX[i], coronaY[i], i)

    #calling injection
        if injection_state=="fire":
            fire_injection(injectionX,injectionY)
            injectionY -= iy


    #injection boundaries
            if injectionY <=0:
                injectionY =420
                injection_state = "ready"



doctor(doctorX,doctorY)
show_score(textX,textY)
pygame.display.update()

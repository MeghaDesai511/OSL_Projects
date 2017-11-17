def draw(n):
    if n == 10:
        print()
        print()
        print()
        print()
    elif n==9:
        print()
        print()
        print()
        print("__")
    elif n==8:
        print()
        print()
        print()
        print("_|_")
    elif n==7:
        print()
        print(" | ")
        print(" | ")
        print("_|_")
    elif n==6:
        print(" ____")
        print(" | ")
        print(" | ")
        print("_|_")
    elif n==5:
        print(" ____")
        print(" |  0")
        print(" | ")
        print("_|_")
    elif n==4:
        print(" ____")
        print(" |  0")
        print(" |  |")
        print("_|_")
    elif n==3:
        print(" ____")
        print(" |  0")
        print(" | -|")
        print("_|_")
    elif n==2:
        print(" ____")
        print(" |  0")
        print(" | -|-")
        print("_|_")
    elif n==1:
        print(" ____")
        print(" |  0")
        print(" | -|-")
        print("_|_-")
    elif n==0:
        print(" ____")
        print(" |  0")
        print(" | -|-")
        print("_|_- -")
        print("DEAD")


import pygame, sys
from pygame.locals import *
def draw(n):
    pygame.init()
    windowSurface = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Hello world!')
    # set up the colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    basicFont = pygame.font.SysFont(None, 48)
    # set up the text
    '''
    text = basicFont.render('Hello world!', True, WHITE, BLUE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery
    '''
    # draw the white background onto the surface
    windowSurface.fill(WHITE)
    '''
    pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
    pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
    pygame.draw.line(windowSurface, BLUE, (90, 60), (120,60), 4)# top line 
    pygame.draw.circle(windowSurface, BLUE, (120, 70), 10, 0)# head
    pygame.draw.line(windowSurface, BLUE, (120, 70), (120,100), 4)# body 
    pygame.draw.line(windowSurface, BLUE, (120, 80), (140,90), 4)# hand1
    pygame.draw.line(windowSurface, BLUE, (120, 80), (100,90), 4)# hand2 
    pygame.draw.line(windowSurface, BLUE, (120, 100), (140,110), 4)# leg1 
    pygame.draw.line(windowSurface, BLUE, (120, 100), (100,110), 4)# leg2 
    '''

    pixArray = pygame.PixelArray(windowSurface)
    pixArray[480][380] = BLACK
    del pixArray

    # draw the text onto the surface
    #windowSurface.blit(text, textRect)

    # draw the window onto the screen
    pygame.display.update()

    # run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    if n == 9:
        print("HII")
    elif n==8:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
    elif n==7:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
        pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
    elif n==6:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
        pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
        pygame.draw.line(windowSurface, BLUE, (90, 60), (120,60), 4)# top line
    elif n==5:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
        pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
        pygame.draw.line(windowSurface, BLUE, (90, 60), (120,60), 4)# top line 
        pygame.draw.circle(windowSurface, BLUE, (120, 70), 10, 0)# head
    elif n==4:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
        pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
        pygame.draw.line(windowSurface, BLUE, (90, 60), (120,60), 4)# top line 
        pygame.draw.circle(windowSurface, BLUE, (120, 70), 10, 0)# head
        pygame.draw.line(windowSurface, BLUE, (120, 70), (120,100), 4)# body 
    elif n==3:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
        pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
        pygame.draw.line(windowSurface, BLUE, (90, 60), (120,60), 4)# top line 
        pygame.draw.circle(windowSurface, BLUE, (120, 70), 10, 0)# head
        pygame.draw.line(windowSurface, BLUE, (120, 70), (120,100), 4)# body 
        pygame.draw.line(windowSurface, BLUE, (120, 80), (140,90), 4)# hand1
    elif n==2:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
        pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
        pygame.draw.line(windowSurface, BLUE, (90, 60), (120,60), 4)# top line 
        pygame.draw.circle(windowSurface, BLUE, (120, 70), 10, 0)# head
        pygame.draw.line(windowSurface, BLUE, (120, 70), (120,100), 4)# body 
        pygame.draw.line(windowSurface, BLUE, (120, 80), (140,90), 4)# hand1
        pygame.draw.line(windowSurface, BLUE, (120, 80), (100,90), 4)# hand2 
    elif n==1:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
        pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
        pygame.draw.line(windowSurface, BLUE, (90, 60), (120,60), 4)# top line 
        pygame.draw.circle(windowSurface, BLUE, (120, 70), 10, 0)# head
        pygame.draw.line(windowSurface, BLUE, (120, 70), (120,100), 4)# body 
        pygame.draw.line(windowSurface, BLUE, (120, 80), (140,90), 4)# hand1
        pygame.draw.line(windowSurface, BLUE, (120, 80), (100,90), 4)# hand2 
        pygame.draw.line(windowSurface, BLUE, (120, 100), (140,110), 4)# leg1 
    elif n==0:
        print(n)
        pygame.display.flip()
        pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)#down line _
        pygame.draw.line(windowSurface, BLUE, (90, 120), (90, 60),4)# stand |
        pygame.draw.line(windowSurface, BLUE, (90, 60), (120,60), 4)# top line 
        pygame.draw.circle(windowSurface, BLUE, (120, 70), 10, 0)# head
        pygame.draw.line(windowSurface, BLUE, (120, 70), (120,100), 4)# body 
        pygame.draw.line(windowSurface, BLUE, (120, 80), (140,90), 4)# hand1
        pygame.draw.line(windowSurface, BLUE, (120, 80), (100,90), 4)# hand2 
        pygame.draw.line(windowSurface, BLUE, (120, 100), (140,110), 4)# leg1 
        pygame.draw.line(windowSurface, BLUE, (120, 100), (100,110), 4)# leg2



#importing the time module
import time
from random import randint

name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

word_list =['note','whole','waste','crime','petite','ritzy','thinkable','savory','sofa','mysterious','acid','bomb','angry','jeans','quarter','weary','drop','normal','flap','overjoyed','furtive','bath','van','solid','known','hill','periodic','sedate','aunt','parsimonious','kiss','cemetery','unarmed','quack','use','psychotic','righteous','whimsical','absent','short','grip','ignorant','letters','threatening','orange','thankful','rabbits','endurable','delay','pour']
i = randint(0,49)#random selection of word
word = str(word_list[i])

guesses = ''

turns = 9

while turns > 0:         
    # make a counter that starts with zero
    failed = 0             
    
    for char in word:      
        # see if the character is in the players guess
        if char in guesses:    
            print(char),    
        else:    
            print ("_"),     
            failed += 1    

    if failed == 0:        
        print ("You won")  
        break              

    print()

    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    
    draw(turns)
    # if the guess is not found in the secret word
    if guess not in word:  
 
        turns -= 1        
        print ("Wrong")    
        print ("You have", + turns, 'more guesses')
 
        if turns == 0:           
            print ("You Loose!! Try your luck next time!!")

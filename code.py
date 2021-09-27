"""
##################### The Hangman Game #######################

Created using pygame
by Team Moxie
   - Nithi Santhosh
   - Sneha C
   - Chandana R

Hangman is an old school favorite, a word game where the goal is simply to find the missing word or words.
You will be presented with a number of blank spaces representing the missing letters you need to find.
Use the keyboard to guess a letter (I recommend starting with vowels).
If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.
After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.
Be warned, every time you guess a letter wrong you loose a life and the hangman begins to appear, piece by piece.
Solve the puzzle before the hangman dies.

###############################################################
"""

import pygame
import math
import sys
from wonderwords import RandomWord

# Initialize the pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Imitialize variables
Guessed =[]
HangmanStatus = 0
FPS = 60
clock = pygame.time.Clock()

# Title and Icon
pygame.display.set_caption("The Hangman Game")
icon = pygame.image.load("hangman.png")
pygame.display.set_icon(icon)

# create the screen
Width=1000
Height=600
screen = pygame.display.set_mode((Width,Height))

# Background
Background = pygame.image.load("Final background.jpg")
Background = pygame.transform.scale(Background,(1000,600))

# To pick a random word 
w= RandomWord()
word = w.word(word_min_length=4,word_max_length=10)
word = word.upper()

# Fonts
LetterFont = pygame.font.SysFont('Chiller', 40)
WordFont = pygame.font.SysFont('Chiller', 60)
TitleFont = pygame.font.SysFont('Chiller', 70)
Font = pygame.font.SysFont('Chiller',35)
Copyright = pygame.font.SysFont('Ariel',14)

# colours
Black = (0,0,0)
White = (255,255,255)
light = "#FBF5F4"
dark = (100,100,100)

# Sounds
Button = pygame.mixer.Sound("Button Sound.wav")
Fail = pygame.mixer.Sound("Fail Sound.wav")
Win = pygame.mixer.Sound("Win Sound.wav")


Click = False

# Start Screen
def StartScreen():
    
    while True:
        # Display Background
        screen.blit(Background,(0,0))

        # draw title
        text = TitleFont.render("HANGMAN !", 1, Black)
        screen.blit(text, (Width/2 - text.get_width()/2,200)) 

        # Copyright mention
        text = Copyright.render("created by team MOXIE", 1, Black)
        screen.blit(text, (450,580))

        # To get mouse position
        mx, my = pygame.mouse.get_pos()

        # To create button
        Play = pygame.Rect(280, 400, 200, 50)
        HowToPlay = pygame.Rect(550, 400 ,200, 50)
   
        pygame.draw.rect(screen, light, Play)
        pygame.draw.rect(screen, light, HowToPlay)


        Click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True

        if Play.collidepoint((mx, my)):
            pygame.draw.rect(screen,dark,Play)

            # If 'Play' button is clicked, then the game window opens up
            if Click:
                pygame.mixer.Sound.play(Button)
                Game()
        else:
            pygame.draw.rect(screen,light,Play)
            
        
        if HowToPlay.collidepoint((mx, my)):
            pygame.draw.rect(screen,dark,HowToPlay)

            # If 'How To Play' button is clicked, instructions window opens up
            if Click:
                pygame.mixer.Sound.play(Button)
                Instructions()
        else:
            pygame.draw.rect(screen, light,HowToPlay)
        
        # Display text on the buttons
        PlayText = Font.render("Play",1,Black)
        screen.blit(PlayText,(360,400))
        HowToPlayText = Font.render("HowTo Play",1,Black)
        screen.blit(HowToPlayText,(590,400))
        
        pygame.display.update()
        clock.tick(FPS)
        



# To display Instructions of Game
def Instructions():
    
    while True:

        # Displays game instructions
        Instructions = pygame.image.load("instructions.jpg")
        Instructions= pygame.transform.scale(Instructions,(1000,600))
        screen.blit(Instructions,(0,0))

        # To get mouse position
        mx, my = pygame.mouse.get_pos()

        # To create button
        Back = pygame.Rect(800, 50, 100, 50)

        pygame.draw.rect(screen, light, Back)

        Click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True

        if Back.collidepoint((mx, my)):
            pygame.draw.rect(screen,dark,Back)

            # If 'Back' button is clicked, we get directed to start screen
            if Click:
                pygame.mixer.Sound.play(Button)
                StartScreen()
        else:
            pygame.draw.rect(screen,light,Back)

        # Display text on button
        BackText = Font.render("Back",1,Black)
        screen.blit(BackText,(830,50))

        pygame.display.update()


# To Play the Game
def Game():

    # Display Background
    screen.blit(Background,(0,0))

    Main()
    while True:
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(FPS)


# Load Hangman images
images = []
for i in range(10):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# Alaphabet Buttons
Radius = 20
Gap = 15
letters = []
startx = round((Width - (Radius * 2 + Gap) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + Gap * 2 + ((Radius * 2 + Gap) * (i % 13))
    y = starty + ((i // 13) * (Gap + Radius * 2))
    letters.append([x, y, chr(A + i), True])
screen.blit(images[HangmanStatus], (150, 100))
pygame.display.update()

def draw():
    # Draw word
    DisplayWord = ""
    for letter in word:
        if letter in Guessed:
            DisplayWord += letter + " "
        else:
            DisplayWord += "_ "
    text = WordFont.render(DisplayWord, 1, Black)
    screen.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            text = LetterFont.render(ltr, 1, Black)
            screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    screen.blit(images[HangmanStatus], (150, 100))
    pygame.display.update()


# Displays message on screen
def DisplayMessage(message,answer):
    pygame.time.delay(1000)
    screen.blit(Background,(0,0))
    text = TitleFont.render(message, 1, Black)
    Ans = WordFont.render(answer,1 ,Black)
    screen.blit(text, (Width/2 - text.get_width()/2, Height/2 - text.get_height()/2))
    screen.blit(Ans, (250,350))

    pygame.display.update()
    pygame.time.delay(4000)

     
# Main
def Main():
    global HangmanStatus
    run = True
    
    # Game Loop
    while run:

        # Background Image
        screen.blit(Background,(0,0))
        clock.tick(FPS)

        # draw title
        text = TitleFont.render("HANGMAN !", 1, Black)
        screen.blit(text, (Width/2 - text.get_width()/2, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < Radius:
                            pygame.mixer.Sound.play(Button)
                            letter[3] = False
                            Guessed.append(ltr)
                            if ltr not in word:
                                HangmanStatus += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in Guessed:
                won = False
                break
        
        if won:
            pygame.mixer.Sound.play(Win)
            DisplayMessage("You WON!","")
            
            break

        if HangmanStatus == 9:
            pygame.mixer.Sound.play(Fail)
            DisplayMessage("You LOST!","The Correct Word is "+word)
            
            
            break
    
while True:
    StartScreen()

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
from wonderwords import RandomWord

# Initialize the pygame
pygame.init()

Guessed =[]
HangmanStatus = 0

# Title and Icon
pygame.display.set_caption("The Hangman Game")
icon = pygame.image.load("hangman.png")
pygame.display.set_icon(icon)


# create the screen
Width=1000
Height=600
screen = pygame.display.set_mode((Width,Height))

# Background
Background = pygame.image.load("blue grid.jpg")
Background = pygame.transform.scale(Background,(1000,600))



# To pick a random word 
w= RandomWord()
word = w.word(word_min_length=4,word_max_length=6)
word = word.upper()


# Fonts
LetterFond = pygame.font.SysFont('comicsans', 40)
WordFond = pygame.font.SysFont('comicsans', 60)
TitleFond = pygame.font.SysFont('comicsans', 70)

# Load Hangman images
images = []
for i in range(7):
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
    display_word = ""
    for letter in word:
        if letter in Guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WordFond.render(display_word, 1, "#FFFFFF")
    screen.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, "#ffffff", (x, y), Radius, 3)
            text = LetterFond.render(ltr, 1, "#000000")
            screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    screen.blit(images[HangmanStatus], (150, 100))

    pygame.display.update()

 
# Displays message on screen
def display_message(message):
    pygame.time.delay(1000)
    screen.fill("#FFFFFF")
    text = WordFond.render(message, 1, "#FFFFFF","#000000")
    screen.blit(text, (Width/2 - text.get_width()/2, Height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

     
# Main
def main():
    global HangmanStatus

    FPS = 60
    clock = pygame.time.Clock()
    run = True
    
    # Game Loop
    while run:

        # Background Image
        screen.blit(Background,(0,0))
        clock.tick(FPS)

        # draw title
        text = TitleFond.render("HANGMAN", 1, "#FFFFFF")
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
            display_message("You WON!")
            break

        if HangmanStatus == 6:
            display_message("You LOST!")
            break
    
while True:
    
    main()
    pygame.quit()

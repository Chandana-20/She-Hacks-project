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
from wonderwords import RandomWord

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000,600))

# Background
Background = pygame.image.load("blue grid.jpg")
Background = pygame.transform.scale(Background,(1000,600))


# Title and Icon
pygame.display.set_caption("The Hangman Game")
icon = pygame.image.load("hangman.png")
pygame.display.set_icon(icon)

# To pick a random word 
w= RandomWord()
print(w.word(word_min_length=4,word_max_length=6))

# Game Loop
running = True 
while running:

    # Background Image
    screen.blit(Background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

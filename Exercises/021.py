# Create a program in Python that opens and plays the audio from an MP3 file.

import pygame

# Initialize pygame mixer
pygame.init()

# Load the MP3 file
pygame.mixer.music.load('YourMp3Song.mp3')

# Play the MP3 file
pygame.mixer.music.play()

# Keep the program running until the music finishes
pygame.event.wait()

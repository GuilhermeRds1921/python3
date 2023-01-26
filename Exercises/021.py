# Faça um programa em Pyhton que abra e reproduza o áudio de um 
# arquivo MP3.
#Mp3 file required.

import pygame
pygame.init()
pygame.mixer.music.load('YourMp3Song.mp3')
pygame.mixer.music.play()
pygame.event.wait()

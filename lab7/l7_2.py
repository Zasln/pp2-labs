import pygame
import os

pygame.init()
width, height = 700, 700
screen=pygame.display.set_mode((width, height))
clock=pygame.time.Clock()
song_path=r'C:\Users\User\Desktop\Songs'

def get_songs():
    songs=[]
    for file in os.listdir(song_path):
        if file.endswith('.mp3'):
            songs.append(os.path.join(song_path, file))
    return songs
songs=get_songs()
index=0
length_of_song=pygame.mixer.Sound(songs[index]).get_length
pygame.mixer.music.load(songs[index])
pygame.mixer.music.play(0)
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                index+=1
            if event.key == pygame.K_LEFT:
                index-=1
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    
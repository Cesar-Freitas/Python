import pygame
import emoji
# pygame.mixer.init()
# pygame.init()
# pygame.mixer.music.load("PeryCreep_-_lofi_chill_music.mp3")
# pygame.mixer.music.play()
# pygame.mixer.music.set_volume(3)
# x = input("Digite algo para encerrar..")
# -------------------------------------------------------------------
pygame.mixer.init()
pygame.init()
# A linha abaixo deve conter o nome do seu arquivo de áudio
pygame.mixer.music.load("PeryCreep_-_lofi_chill_music.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(2)
x = input(emoji.emojize("Pressione qualquer tecla para encerrar \033[1:31m :x: \033[m", use_aliases=True))

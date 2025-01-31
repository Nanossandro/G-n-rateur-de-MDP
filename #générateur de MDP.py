#générateur de MDP
import pygame
import time
from pygame.locals import *
import random

pygame.init()

screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Générateur de MDP")

police=None

def menu():
    global police
    screen.fill((255, 255, 255))  # Efface l'écran avec une couleur noire
    police=pygame.font.SysFont("8-Bit-Madness",30)
    image_texte = police.render("Bienvenue au générateur de Mot de Passe de NANO", 1, (0,0,0))
    policeinfo=pygame.font.SysFont("8-Bit-Madness",20)
    info = policeinfo.render("Il faut en moyenne 3 ans non stop pour réussir à cracker un de nos mdp", 1, (0,0,0))
    screen.blit(image_texte,(50,20))
    screen.blit(info,(80,450))
    logo = pygame.image.load("4857990.png")
    logo=pygame.transform.scale(logo,(230,230))
    screen.blit(logo,(215,70))

menu()

def generateur():

    mdp = ''.join(random.choices(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')','_','+','-','=','[',']','{','}','|',';',':','<','>','?','/','.',',','0','1','2','3','4','5','6','7','8','9'],k=12))
    txtMdp = police.render("Votre mot de passe est :", 1,(0,0,0))
    MotDePasse = police.render(mdp, 1,(0,0,0))

    imsecu = pygame.image.load("securr.png")
    imsecu=pygame.transform.scale(imsecu,(200,200))
    screen.blit(imsecu,(225,10))
    screen.blit(txtMdp,(200,200))
    screen.blit(MotDePasse,(200,250))
    print(mdp)
   

class Button:
    def __init__(self, x, y, image, text_input):
        global police
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_input = text_input
        self.text =police.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            return self.rect.collidepoint(pos)

boutonsurf = pygame.image.load("oval-23967_1280.webp")
boutonsurf=pygame.transform.scale(boutonsurf,(270,150))

bouton = Button(330, 370,boutonsurf, "Générer un MDP")


running=True
chgmtimage = False

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
        elif event.type == MOUSEBUTTONDOWN :
            if bouton.is_clicked(event.pos):
                chgmtimage = True

    if chgmtimage:
        screen.fill((255,255,255))
        generateur()
        chgmtimage = False

    bouton.update()
    pygame.display.flip()

pygame.quit()
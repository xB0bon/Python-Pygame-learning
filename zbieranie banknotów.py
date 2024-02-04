import pygame
import random


class Player:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.speed = 8
        self.image = pygame.image.load("player (Niestandardowe).png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):  # wykonuje się raz na powtórzenie pętli while
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y_cord > 0:
            self.y_cord -= self.speed

        if keys[pygame.K_s] and self.y_cord < 500:
            self.y_cord += self.speed

        if keys[pygame.K_a] and self.x_cord > 0:
            self.x_cord -= self.speed

        if keys[pygame.K_d] and self.x_cord < 1150:
            self.x_cord += self.speed

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)  # hitboxy muszą być ciągle
        # odswiezane

    def draw(self):  # jest odpowiedzialna za rysowanie gracza na ekrania
        window.blit(self.image, (self.x_cord, self.y_cord))


class Banknot:
    def __init__(self):
        self.image = pygame.image.load("banknot (Niestandardowe).png")
        self.x_cord = random.randint(1, 1150)
        self.y_cord = random.randint(1, 550)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width,
                                  self.height)  # hitboxy muszą być ciągle odswiezane

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


pygame.init()
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("First game in Pygame")


# image = pygame.image.load("obrazek.jfif")
# window.blit(image, (0, 0))

def main():
    running = True
    player = Player()
    clock = 0
    banknotes = []
    score = 0
    background = pygame.image.load("background.jfif")

    while running:
        text = pygame.font.Font.render(pygame.font.SysFont("Arial", 48), f"score: {score}", True, (255, 255, 255))
        clock += pygame.time.Clock().tick(60) / 1000  # gra powtórzy się tyle razy na sekunde. zwalnia postać
        for event in pygame.event.get():  # zdarzenia wykonane przez gracza
            if event.type == pygame.QUIT:  # Jeśli gracz zamknie okienko
                running = False
        if clock >= 1:
            clock = 0
            banknotes.append(Banknot())

        player.tick()

        for banknote in banknotes:
            banknote.tick()

        for banknote in banknotes:
            if player.hitbox.colliderect(banknote.hitbox):
                score += 1
                banknotes.remove(banknote)
                print(score)

        window.blit(background, (0,0))  # zmienie koloru tła. Dodawanie tła

        player.draw()
        for banknote in banknotes:
            banknote.draw()
        window.blit(text, (500, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()

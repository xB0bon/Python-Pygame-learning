import pygame


class Physic():
    def __init__(self, acc, max_vel):
        self.hor_velocity = 0  # prędkość w poziomie
        self.ver_velocity = 0  # prędkość w pionie
        self.acc = acc  # Przyspieszenie
        self.max_vel = max_vel  # max prędkość

    def physic_tick(self):
        self.ver_velocity += 0.7


class Player(Physic):
    def __init__(self):
        super().__init__(0.5, 5)  # łączy player z phycisc
        self.x_cord = 0
        self.y_cord = 580
        self.image = pygame.image.load("john.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, keys):  # wykonuje się raz na powtórzenie pętli whileddd
        self.physic_tick()
        if keys[pygame.K_a] and self.hor_velocity > self.max_vel * -1:
            self.hor_velocity -= self.acc

        if keys[pygame.K_d] and self.hor_velocity < self.max_vel:
            self.hor_velocity += self.acc

        if not (keys[pygame.K_a] or keys[pygame.K_d]):
            if self.hor_velocity < 0:
                self.hor_velocity += self.acc

            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
        self.x_cord += self.hor_velocity
        self.y_cord -= self.hor_velocity
        print(self.hor_velocity)

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)  # hitboxy muszą być ciągle
        # odswiezane

    def draw(self):  # jest odpowiedzialna za rysowanie gracza na ekrania
        window.blit(self.image, (self.x_cord, self.y_cord))


pygame.init()
window = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("First game in Pygame")


# image = pygame.image.load("obrazek.jfif")
# window.blit(image, (0, 0))

def main():
    running = True
    player = Player()
    clock = 0
    background = pygame.image.load("polana.png")

    while running:
        clock += pygame.time.Clock().tick(60) / 1000  # gra powtórzy się tyle razy na sekunde. zwalnia postać
        for event in pygame.event.get():  # zdarzenia wykonane przez gracza
            if event.type == pygame.QUIT:  # Jeśli gracz zamknie okienko
                running = False
        keys = pygame.key.get_pressed()
        player.tick(keys)

        window.blit(background, (0, 0))  # zmienie koloru tła. Dodawanie tła

        player.draw()

        pygame.display.update()


if __name__ == "__main__":
    main()

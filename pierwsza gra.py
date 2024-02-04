import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("First game in Pygame")

x = 0
y = 0

player = pygame.rect.Rect(x, y, 100, 100)  # x, y = położenie klocka, 100, 100 - wielkość klocka

running = True

while running:
    pygame.time.Clock().tick(60)  # gra powtórzy się tyle razy na sekunde. zwalnia postać
    for event in pygame.event.get():  # zdarzenia wykonane przez gracza
        if event.type == pygame.QUIT:  # Jeśli gracz zamknie okienko
            running = False

    keys = pygame.key.get_pressed()
    speed = 10
    if keys[pygame.K_w]:  # po kliknieciu w
        y -= speed

    if keys[pygame.K_s]:  # po kliknieciu s
        y += speed

    if keys[pygame.K_a]:  # po kliknieciu a
        x -= speed

    if keys[pygame.K_d]:  # po kliknieciu d
        x += speed

    player = pygame.rect.Rect(x, y, 100, 100)  # konieczne

    window.fill((0, 153, 255))  # zmienie koloru tła. Dodawanie tła
    pygame.draw.rect(window, (51, 204, 51), player)  # dodawanie gracza
    pygame.display.update()

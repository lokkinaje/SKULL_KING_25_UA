import pygame
pygame.init()

# Fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Skull King")

# Couleurs
VERT = (0, 255, 0)
BLANC = (255, 255, 255)

# Carte (remplace par ton image réelle)
image_carte = pygame.image.load("cartes_sk/arriere_carte.png").convert_alpha()
image_carte = pygame.transform.scale(image_carte, (100, 150))

class Carte:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.original_y = y
        self.rect = pygame.Rect(x, y, 100, 150)
        self.selected = False

    def draw(self, surface):
        # Surélève la carte si sélectionnée
        y_offset = -20 if self.selected else 0
        surface.blit(image_carte, (self.x, self.y + y_offset))

        # Liseré vert
        if self.selected:
            pygame.draw.rect(surface, VERT, (self.x, self.y + y_offset, 100, 150), 3)

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            self.selected = not self.selected
        else:
            self.selected = False

# Initialisation d’une carte
ma_carte = Carte(350, 400)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((200, 200, 200))  # Fond gris clair

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Clique sur la carte
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ma_carte.handle_click(event.pos)

        # Validation avec espace
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN)   and ma_carte.selected:
                print("Carte validée !")

    # Affichage
    ma_carte.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
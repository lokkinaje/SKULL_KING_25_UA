import pygame 

class Button :
    def __init__(self , chemin_image , position  , scale = 1 ) : 
        self.image = pygame.image.load(chemin_image).convert_alpha()

        original_width  = self.image.get_width()
        original_height = self.image.get_height()
        new_width = int (original_width * scale )
        new_height = int (original_height * scale )

        self.image = pygame.transform.smoothscale(self.image , (new_width , new_height))

        self.rect = self.image.get_rect(topleft = position )

    def draws(self , window) : 
        window.blit(self.image , self.rect)

    def est_presser(self) : 
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos) : 
            if mouse_pressed : 
                return True 
        return False 
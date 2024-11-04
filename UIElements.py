import pygame

class RoundedTextBox:
    def __init__(self, text, font, canvas_width, canvas_height, box_size, corner_radius=20):
        self.text = text
        self.font = font
        self.box_size = box_size
        self.corner_radius = corner_radius

        self.position = (
            (canvas_width - self.box_size[0]) // 2,  
            (canvas_height - self.box_size[1]) // 2 - 300 
        )

        self.text_surface = self.font.render(self.text, True, (255, 255, 255))  

    def draw(self, surface):
        glass_color = (255, 255, 255, 100)  
        glass_surface = pygame.Surface(self.box_size, pygame.SRCALPHA)
        glass_surface.fill((0, 0, 0, 0)) 

        rect = pygame.Rect(0, 0, *self.box_size)
        pygame.draw.rect(glass_surface, glass_color, rect, border_radius=self.corner_radius)

        text_x = (self.box_size[0] - self.text_surface.get_width()) // 2
        text_y = (self.box_size[1] - self.text_surface.get_height()) // 2
        glass_surface.blit(self.text_surface, (text_x, text_y))

        surface.blit(glass_surface, self.position)

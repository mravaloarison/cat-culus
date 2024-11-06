import pygame

class RoundedTextBox:
    def __init__(self, text, font, canvas_width, canvas_height, box_size, corner_radius=20):
        self.text = text
        self.font = font
        self.corner_radius = corner_radius

        self.max_width = int(canvas_width * 0.6)
        
        self.text_lines = self.wrap_text(self.text, self.max_width)
        self.line_height = self.font.get_linesize()
        self.box_size = (self.max_width, len(self.text_lines) * self.line_height + 20) 

        self.position = (
            (canvas_width - self.box_size[0]) // 2,  
            (canvas_height - self.box_size[1]) // 2 - 200 
        )

    def wrap_text(self, text, max_width):
        """Wrap text into multiple lines to fit within the specified max width."""
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "

        lines.append(current_line.strip())  
        return lines

    def draw(self, surface):
        glass_color = (255, 255, 255, 100)  
        glass_surface = pygame.Surface(self.box_size, pygame.SRCALPHA)
        glass_surface.fill((0, 0, 0, 0)) 

        rect = pygame.Rect(0, 0, *self.box_size)
        pygame.draw.rect(glass_surface, glass_color, rect, border_radius=self.corner_radius)

        for i, line in enumerate(self.text_lines):
            text_surface = self.font.render(line, True, (255, 255, 255))
            text_x = (self.box_size[0] - text_surface.get_width()) // 2
            text_y = 10 + i * self.line_height 
            glass_surface.blit(text_surface, (text_x, text_y))

        surface.blit(glass_surface, self.position)

    def remove(self, surface):
        surface.fill((0, 0, 0), (self.position, self.box_size))
        pygame.display.update()



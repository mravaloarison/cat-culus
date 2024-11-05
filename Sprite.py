import pygame

class Sprite:
    def __init__(self, image_path, scale_factor=1, num_frames=1, sprite_width=0, sprite_height=0):
        self.sheet = pygame.image.load(image_path)
        self.sprite_width = sprite_width / num_frames
        self.sprite_height = sprite_height
        self.scaled_width = self.sprite_width * scale_factor
        self.scaled_height = self.sprite_height * scale_factor
        self.num_frames = num_frames
        self.idle_frames = self.load_frames(0, self.num_frames)

    def load_frames(self, start_frame, num_frames):
        frames = []
        for i in range(start_frame, num_frames):
            frame = self.sheet.subsurface((i * self.sprite_width, 0, self.sprite_width, self.sprite_height))
            scaled_frame = pygame.transform.scale(frame, (self.scaled_width, self.scaled_height))
            frames.append(scaled_frame)
        return frames
    
    def get_frame(self):
        return self.idle_frames
    

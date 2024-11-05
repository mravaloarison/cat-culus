import pygame

class Thunder:
    def __init__(self, image_path, scale_factor=1):
        self.sheet = pygame.image.load(image_path)
        self.sprite_width = 1821 / 8
        self.sprite_height = 290
        self.scaled_width = self.sprite_width * scale_factor
        self.scaled_height = self.sprite_height * scale_factor
        self.num_frames_idle = 5
        self.num_frames_hit = 8
        self.idle_frames = self.load_frames(0, self.num_frames_idle)
        self.hit_frames = self.load_frames(5, self.num_frames_hit)
    
    def load_frames(self, start_frame, num_frames):
        frames = []
        for i in range(start_frame, num_frames):
            frame = self.sheet.subsurface((i * self.sprite_width, 0, self.sprite_width, self.sprite_height))
            scaled_frame = pygame.transform.scale(frame, (self.scaled_width, self.scaled_height))
            frames.append(scaled_frame)
        return frames
    
    def get_idle_frames(self):
        return self.idle_frames
    
    def get_hit_frames(self):
        return self.hit_frames
import pygame, random
import Setup as sp

class Thunder:
    def __init__(self, image_path, scale_factor=1):
        self.sheet = pygame.image.load(image_path)
        self.sprite_width = 1204 / 10
        self.sprite_height = 300
        self.scaled_width = self.sprite_width * scale_factor
        self.scaled_height = self.sprite_height * scale_factor
        self.num_frames_idle = 5
        self.num_frames_hit = 10
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

class ThunderManager:
    def __init__(self, thunder_sprite, target_position, speed=9, hit_duration=500):
        self.thunder = thunder_sprite  
        self.target_position = target_position
        self.speed = speed
        self.hit_duration = hit_duration
        self.current_position = self.generate_random_position()
        self.reached_target = False
        self.hit_animation_start_time = None
        self.was_hit = False

    def generate_random_position(self):
        corner_choice = random.choice(['top', 'left', 'right'])
        if corner_choice == 'top':
            x = random.randint(0, sp.GAME_WIDTH)
            y = random.randint(0, sp.GAME_HEIGHT // 2 - 300)
        elif corner_choice == 'left':
            x = random.randint(0, 100)
            y = random.randint(0, sp.GAME_HEIGHT // 2)
        else:  
            x = random.randint(sp.GAME_WIDTH - 100, sp.GAME_WIDTH)
            y = random.randint(0, sp.GAME_HEIGHT // 2)
        return [x, y]

    def update(self, current_time):
        if self.was_hit:
            if self.hit_animation_start_time is None:
                self.hit_animation_start_time = current_time  

            if current_time - self.hit_animation_start_time < self.hit_duration:
                sp.isCatAttack = True
                frame_index = (current_time // 100) % 5
                return self.thunder.get_hit_frames()[int(frame_index)], self.current_position
            else:
                self.hit_animation_start_time = None
                self.reached_target = False
                self.was_hit = False
                self.current_position = self.generate_random_position()
                sp.isCatAttack = False
                return None, None

        elif not self.reached_target:
            dx = self.target_position[0] - self.current_position[0]
            dy = self.target_position[1] - self.current_position[1]
            distance = (dx**2 + dy**2)**0.5

            if distance > self.speed:
                self.current_position[0] += self.speed * (dx / distance)
                self.current_position[1] += self.speed * (dy / distance)
            else:
                self.reached_target = True  

            frame_index = (current_time // 100) % self.thunder.num_frames_idle
            return self.thunder.get_idle_frames()[int(frame_index)], self.current_position
        else:
            if self.hit_animation_start_time is None:
                self.hit_animation_start_time = current_time

            if current_time - self.hit_animation_start_time < self.hit_duration:
                sp.isCatHit = True
                frame_index = (current_time // 100) % 5
                return self.thunder.get_hit_frames()[int(frame_index)], self.target_position
            else:
                self.hit_animation_start_time = None
                self.reached_target = False
                self.was_hit = False
                self.current_position = self.generate_random_position()
                sp.isCatHit = False
                sp.hearts_used += 1
                return None, None

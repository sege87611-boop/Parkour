"""
Player Class - Handles player physics, movement, and state
"""

import pygame
import math


class Player:
    """Player character with parkour mechanics."""
    
    def __init__(self, x, y):
        """Initialize player."""
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.8
        self.max_speed = 8
        self.gravity = 0.6
        self.jump_power = 15
        self.max_velocity_y = 20
        self.is_jumping = False
        self.is_falling = False
        self.is_on_ground = False
        self.is_on_wall = False
        self.wall_side = None  # 'left' or 'right'
        self.double_jump_available = True
        self.coins = 0
        self.color = (100, 200, 255)
        self.animation_frame = 0
        self.spawn_x = x
        self.spawn_y = y
    
    def move_left(self):
        """Move player left."""
        self.velocity_x -= self.acceleration
        self.velocity_x = max(self.velocity_x, -self.max_speed)
    
    def move_right(self):
        """Move player right."""
        self.velocity_x += self.acceleration
        self.velocity_x = min(self.velocity_x, self.max_speed)
    
    def jump(self):
        """Handle jump action."""
        if self.is_on_ground:
            self.velocity_y = -self.jump_power
            self.is_jumping = True
            self.is_on_ground = False
            self.double_jump_available = True
        elif self.is_on_wall and self.velocity_y < 0:
            # Wall jump
            self.velocity_y = -self.jump_power
            if self.wall_side == 'left':
                self.velocity_x = self.max_speed * 0.8
            else:
                self.velocity_x = -self.max_speed * 0.8
            self.is_on_wall = False
            self.is_jumping = True
        elif self.double_jump_available and self.is_falling:
            # Double jump
            self.velocity_y = -self.jump_power * 0.8
            self.double_jump_available = False
            self.is_jumping = True
    
    def climb(self):
        """Handle wall climbing."""
        if self.is_on_wall:
            self.velocity_y -= 2
            if self.velocity_y < -5:
                self.velocity_y = -5
    
    def update(self, level):
        """Update player physics and state."""
        # Apply gravity
        if not self.is_on_wall:
            self.velocity_y += self.gravity
            self.velocity_y = min(self.velocity_y, self.max_velocity_y)
        else:
            # Slow fall on wall
            if self.velocity_y > 0:
                self.velocity_y *= 0.8
        
        # Friction
        if self.is_on_ground:
            self.velocity_x *= 0.85
        
        # Update position
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Reset ground state
        self.is_on_ground = False
        self.is_on_wall = False
        self.is_falling = self.velocity_y > 1
        
        # Boundary checking
        if self.x < 0:
            self.x = 0
            self.velocity_x = 0
        if self.x + self.width > 1200:
            self.x = 1200 - self.width
            self.velocity_x = 0
        
        # Death pit
        if self.y > 900:
            self.reset(self.spawn_x, self.spawn_y)
    
    def get_rect(self):
        """Get player collision rectangle."""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def reset(self, x, y):
        """Reset player to spawn position."""
        self.x = x
        self.y = y
        self.spawn_x = x
        self.spawn_y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_on_ground = False
        self.is_on_wall = False
        self.double_jump_available = True
        self.coins = 0
    
    def draw(self, surface):
        """Draw player to screen."""
        rect = self.get_rect()
        pygame.draw.rect(surface, self.color, rect)
        
        # Draw eyes
        eye_y = self.y + 15
        if self.velocity_x < 0:
            pygame.draw.circle(surface, (0, 0, 0), (int(self.x + 10), int(eye_y)), 3)
        else:
            pygame.draw.circle(surface, (0, 0, 0), (int(self.x + 20), int(eye_y)), 3)
        
        # Draw animation
        self.animation_frame += 1

"""
Sprites - Visual game objects
"""

import pygame
import math


class Platform:
    """A solid platform that the player can stand on."""
    
    def __init__(self, x, y, width, height, color=(100, 100, 100)):
        """Initialize platform."""
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def collide(self, player_rect, player):
        """Handle collision with player."""
        if player_rect.colliderect(self.rect):
            # Determine collision side
            # Coming from above
            if player.velocity_y > 0 and player_rect.bottom <= self.rect.top + 10:
                player.y = self.rect.top - player.height
                player.velocity_y = 0
                player.is_on_ground = True
                player.double_jump_available = True
            # Coming from below
            elif player.velocity_y < 0 and player_rect.top >= self.rect.bottom - 10:
                player.y = self.rect.bottom
                player.velocity_y = 0
            # Coming from left
            elif player.velocity_x > 0 and player_rect.right <= self.rect.left + 10:
                player.x = self.rect.left - player.width
                player.is_on_wall = True
                player.wall_side = 'left'
            # Coming from right
            elif player.velocity_x < 0 and player_rect.left >= self.rect.right - 10:
                player.x = self.rect.right
                player.is_on_wall = True
                player.wall_side = 'right'
    
    def get_rect(self):
        """Get platform rectangle."""
        return self.rect
    
    def draw(self, surface):
        """Draw platform."""
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (50, 50, 50), self.rect, 2)  # Border


class Spike:
    """A dangerous spike obstacle."""
    
    def __init__(self, x, y, width, height):
        """Initialize spike."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)
    
    def get_rect(self):
        """Get spike rectangle."""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, surface):
        """Draw spike as triangles."""
        rect = self.get_rect()
        # Draw multiple spike triangles
        spike_width = self.width // 4
        for i in range(4):
            x_offset = i * spike_width
            points = [
                (self.x + x_offset, self.y + self.height),
                (self.x + x_offset + spike_width // 2, self.y),
                (self.x + x_offset + spike_width, self.y + self.height)
            ]
            pygame.draw.polygon(surface, self.color, points)


class Coin:
    """A collectable coin."""
    
    def __init__(self, x, y):
        """Initialize coin."""
        self.x = x
        self.y = y
        self.radius = 8
        self.color = (255, 215, 0)  # Gold
        self.bob_offset = 0
        self.bob_speed = 0.1
    
    def get_rect(self):
        """Get coin rectangle."""
        return pygame.Rect(self.x - self.radius, self.y - self.radius + self.bob_offset, 
                          self.radius * 2, self.radius * 2)
    
    def update(self):
        """Update coin animation."""
        self.bob_offset += self.bob_speed
    
    def draw(self, surface):
        """Draw coin."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y + self.bob_offset)), self.radius)
        pygame.draw.circle(surface, (200, 170, 0), (int(self.x), int(self.y + self.bob_offset)), self.radius, 2)


class Goal:
    """The goal/finish point."""
    
    def __init__(self, x, y):
        """Initialize goal."""
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (0, 255, 0)
        self.rotation = 0
    
    def get_rect(self):
        """Get goal rectangle."""
        return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, 
                          self.width, self.height)
    
    def update(self):
        """Update goal animation."""
        self.rotation += 5
    
    def draw(self, surface):
        """Draw goal as a rotating square."""
        rect = self.get_rect()
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, (0, 200, 0), rect, 3)
        
        # Draw star in center
        center_x = self.x
        center_y = self.y
        pygame.draw.circle(surface, (255, 255, 255), (int(center_x), int(center_y)), 8)

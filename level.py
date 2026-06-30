"""
Level Class - Handles level design, platform management, and collision detection
"""

import pygame
from sprites import Platform, Spike, Coin, Goal


class Level:
    """Represents a single game level."""
    
    def __init__(self, number, name, layout):
        """Initialize level."""
        self.number = number
        self.name = name
        self.platforms = []
        self.spikes = []
        self.coins = []
        self.goal = None
        self.walls = []
        
        # Parse layout
        for item in layout:
            if item["type"] == "platform":
                self.platforms.append(Platform(item["x"], item["y"], item["width"], item["height"]))
            elif item["type"] == "spike":
                self.spikes.append(Spike(item["x"], item["y"], item["width"], item["height"]))
            elif item["type"] == "coin":
                self.coins.append(Coin(item["x"], item["y"]))
            elif item["type"] == "goal":
                self.goal = Goal(item["x"], item["y"])
            elif item["type"] == "wall":
                self.walls.append(Platform(item["x"], item["y"], item["width"], item["height"], color=(139, 69, 19)))
    
    def check_collisions(self, player):
        """Check player collisions with level objects."""
        player_rect = player.get_rect()
        
        # Check platform collisions
        for platform in self.platforms + self.walls:
            platform.collide(player_rect, player)
        
        # Check spike collisions
        for spike in self.spikes:
            if player_rect.colliderect(spike.get_rect()):
                player.reset(player.spawn_x, player.spawn_y)
        
        # Check coin collisions
        coins_to_remove = []
        for coin in self.coins:
            if player_rect.colliderect(coin.get_rect()):
                player.coins += 1
                coins_to_remove.append(coin)
        for coin in coins_to_remove:
            self.coins.remove(coin)
    
    def check_goal(self, player):
        """Check if player reached the goal."""
        if self.goal:
            return player.get_rect().colliderect(self.goal.get_rect())
        return False
    
    def draw(self, surface):
        """Draw level to screen."""
        # Draw platforms
        for platform in self.platforms:
            platform.draw(surface)
        
        # Draw walls
        for wall in self.walls:
            wall.draw(surface)
        
        # Draw spikes
        for spike in self.spikes:
            spike.draw(surface)
        
        # Draw coins
        for coin in self.coins:
            coin.draw(surface)
        
        # Draw goal
        if self.goal:
            self.goal.draw(surface)

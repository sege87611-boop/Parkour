"""
Main Game Class - Handles game loop, rendering, and state management
"""

import pygame
from player import Player
from level import Level
from ui import GameUI


class Game:
    """Main game controller."""
    
    def __init__(self):
        """Initialize the game."""
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.FPS = 60
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Parkour Game 🏃‍♂️")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game state
        self.current_level = 0
        self.levels = self.create_levels()
        self.level = self.levels[self.current_level]
        self.player = Player(100, 400)
        
        # UI
        self.ui = GameUI()
        self.font = pygame.font.Font(None, 36)
        
    def create_levels(self):
        """Create all game levels."""
        levels = [
            Level(1, "Introduction", [
                {"type": "platform", "x": 0, "y": 700, "width": 1200, "height": 100},
                {"type": "platform", "x": 300, "y": 600, "width": 200, "height": 20},
                {"type": "platform", "x": 700, "y": 550, "width": 200, "height": 20},
                {"type": "platform", "x": 1100, "y": 500, "width": 100, "height": 20},
                {"type": "coin", "x": 350, "y": 550},
                {"type": "coin", "x": 750, "y": 500},
                {"type": "goal", "x": 1150, "y": 400},
            ]),
            Level(2, "Wall Jump Challenge", [
                {"type": "platform", "x": 0, "y": 700, "width": 1200, "height": 100},
                {"type": "platform", "x": 100, "y": 600, "width": 150, "height": 20},
                {"type": "wall", "x": 350, "y": 400, "width": 50, "height": 200},
                {"type": "platform", "x": 450, "y": 500, "width": 200, "height": 20},
                {"type": "wall", "x": 700, "y": 300, "width": 50, "height": 400},
                {"type": "platform", "x": 800, "y": 400, "width": 150, "height": 20},
                {"type": "coin", "x": 150, "y": 550},
                {"type": "coin", "x": 725, "y": 250},
                {"type": "goal", "x": 850, "y": 350},
            ]),
            Level(3, "Spike Gauntlet", [
                {"type": "platform", "x": 0, "y": 700, "width": 1200, "height": 100},
                {"type": "platform", "x": 100, "y": 600, "width": 150, "height": 20},
                {"type": "spike", "x": 300, "y": 680, "width": 100, "height": 20},
                {"type": "platform", "x": 450, "y": 500, "width": 150, "height": 20},
                {"type": "spike", "x": 650, "y": 580, "width": 100, "height": 20},
                {"type": "platform", "x": 800, "y": 400, "width": 150, "height": 20},
                {"type": "spike", "x": 1000, "y": 480, "width": 100, "height": 20},
                {"type": "coin", "x": 125, "y": 550},
                {"type": "coin", "x": 525, "y": 450},
                {"type": "coin", "x": 875, "y": 350},
                {"type": "goal", "x": 1050, "y": 350},
            ]),
        ]
        return levels
    
    def handle_events(self):
        """Handle user input and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r:
                    self.reset_level()
                elif event.key == pygame.K_n:
                    self.next_level()
    
    def update(self):
        """Update game state."""
        keys = pygame.key.get_pressed()
        
        # Player input
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_SPACE]:
            self.player.jump()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.climb()
        
        # Update player
        self.player.update(self.level)
        
        # Check collisions
        self.level.check_collisions(self.player)
        
        # Check level completion
        if self.level.check_goal(self.player):
            self.next_level()
    
    def render(self):
        """Render game state to screen."""
        self.screen.fill((135, 206, 235))  # Sky blue
        
        # Draw level
        self.level.draw(self.screen)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw UI
        self.ui.draw(self.screen, self.current_level + 1, self.level.name, self.player.coins)
        
        pygame.display.flip()
    
    def next_level(self):
        """Advance to next level."""
        self.current_level += 1
        if self.current_level >= len(self.levels):
            self.show_victory()
            self.current_level = 0
        
        self.level = self.levels[self.current_level]
        self.player.reset(100, 400)
    
    def reset_level(self):
        """Reset current level."""
        self.player.reset(100, 400)
    
    def show_victory(self):
        """Display victory screen."""
        self.screen.fill((0, 0, 0))
        text = self.font.render("🎉 YOU WON! 🎉", True, (255, 255, 0))
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        
        # Wait for input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    waiting = False
    
    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.FPS)

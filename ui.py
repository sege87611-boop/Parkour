"""
UI - User interface elements
"""

import pygame


class GameUI:
    """Game user interface."""
    
    def __init__(self):
        """Initialize UI."""
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
    
    def draw(self, surface, level, level_name, coins):
        """Draw UI elements."""
        # Level info
        level_text = self.font_medium.render(f"Level {level}: {level_name}", True, (0, 0, 0))
        surface.blit(level_text, (20, 20))
        
        # Coins
        coins_text = self.font_medium.render(f"Coins: {coins}", True, (255, 215, 0))
        surface.blit(coins_text, (20, 60))
        
        # Controls hint
        controls = [
            "A/D: Move",
            "SPACE: Jump",
            "UP: Climb",
            "R: Restart"
        ]
        for i, control in enumerate(controls):
            text = self.font_small.render(control, True, (50, 50, 50))
            surface.blit(text, (1200 - 150, 20 + i * 25))

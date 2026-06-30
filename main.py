#!/usr/bin/env python3
"""
Parkour Game - Main Entry Point
A 2D parkour platformer with smooth physics and progressive levels
"""

import pygame
import sys
from game import Game


def main():
    """Initialize and run the parkour game."""
    # Initialize Pygame
    pygame.init()
    
    # Create game instance
    game = Game()
    
    # Run game loop
    game.run()
    
    # Cleanup
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

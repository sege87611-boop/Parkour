# Parkour Game 🏃‍♂️

A fun 2D parkour platformer game built with Python and Pygame.

## Features

- **Smooth Movement**: Run, jump, and perform parkour tricks
- **Wall Climbing**: Scale walls to reach high places
- **Multiple Levels**: Progressive difficulty with varied challenges
- **Collectibles**: Gather coins and power-ups
- **Smooth Physics**: Realistic gravity and momentum
- **Visual Polish**: Animated sprites and particle effects

## Installation

### Requirements
- Python 3.8+
- Pygame

### Setup

```bash
pip install pygame
python main.py
```

## Controls

- **A/D** or **Left/Right Arrow**: Move left/right
- **Space**: Jump
- **Up Arrow/W**: Climb wall (when touching a wall)
- **R**: Restart level
- **ESC**: Quit

## Game Mechanics

### Movement
- **Running**: Smooth acceleration and deceleration
- **Jumping**: Double jump available in air
- **Wall Jump**: Jump off walls to reach higher areas
- **Dashing**: Perform a quick dash forward (limited uses per jump)

### Obstacles
- **Platforms**: Basic solid surfaces
- **Spikes**: Instant death - avoid at all costs!
- **Moving Platforms**: Challenging dynamic obstacles
- **Lava Pits**: Deep pits that reset your progress

### Collectibles
- **Coins**: Earn points
- **Speed Boost**: Temporarily increase movement speed
- **Double Jump**: Temporary extra mid-air jump

## Development

The game is structured with:
- `main.py`: Game loop and initialization
- `player.py`: Player physics and controls
- `level.py`: Level design and management
- `sprites.py`: Visual game objects
- `physics.py`: Physics engine

## License

MIT License - Feel free to use and modify!

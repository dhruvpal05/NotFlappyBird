# NotFlappyBird
NotFlappyBird is a Python-based game inspired by the classic Flappy Bird. Using the Pygame library, players control a bird by pressing the space bar to navigate through oncoming pipes. The objective is to avoid collisions with pipes and the screen edges to achieve the highest score possible. The game features a scoring system that tracks and displays the player's current score and high score. With simple controls and engaging gameplay, NotFlappyBird offers a fun and challenging experience for players of all ages.
## Setup

1. **Clone the Repository**: 

   ```bash
   git clone https://github.com/yourusername/NotFlappyBird.git
   ```

2. **Download Assets**: Ensure you have the necessary asset files (`bg.png`, `bird.png`, `pipet.png`, `pipeb.png`) placed in the `Assets` directory. These files are required for the game to run correctly.

3. **Run the Game**: Navigate to the project directory and run the game with:

   ```bash
   python game.py
   ```

   Note: Replace `game.py` with the filename of your script if it's named differently.

## Controls

- **Space Bar**: Flap the bird to make it go up.
- **Quit**: Close the game window to exit the game.

## Code Overview

- **Initialization**: The game initializes Pygame and sets up the screen, background, fonts, and initial game variables.
- **Pipe Management**: Pipes are created and moved across the screen. Collisions with pipes or screen edges are checked to end the game.
- **Bird Movement**: The bird's position and rotation are managed using gravity and user input.
- **Scoring System**: The game tracks and displays the current score and high score.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Pygame](https://www.pygame.org/) - The library used for creating the game.

---

Enjoy playing NotFlappyBird!
```

Replace placeholders like `https://github.com/yourusername/NotFlappyBird.git` with the actual URL of your repository, and ensure you add or update any specific details relevant to your project.
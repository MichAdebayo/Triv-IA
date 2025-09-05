# Triv-IA

Triv-IA is a command-line trivia game inspired by Trivial Pursuit, designed for multiple players. The game tests your knowledge in various categories related to IT, AI, and more, with a fun board and emoji avatars.

## Features

- Play with 1 to 6 players, each assigned a random emoji avatar.
- Move around a board with different categories and special "Camembert" (wedge) spaces.
- Answer multiple-choice questions from a JSON file, organized by category.
- Collect colored camemberts by answering correctly on special spaces.
- The first player to collect all camemberts wins!

## Game Categories

- Bases de données (Databases)
- Python
- Actualités IA (AI News)
- Lignes de commandes: Unix (Unix Commands)
- Personnalités de l'IA (AI Personalities)
- DevOps

## How to Play

1. **Start the Game**  
   Run the main script:

   ```bash
   python main.py
   ```

2. **Player Setup**  
   - Enter the number of players (1-6).
   - Each player enters their name and age.
   - Each player is assigned a random emoji avatar.

3. **Gameplay Loop**  
   - Players take turns rolling a die and moving around the board.
   - On each turn, the player lands on a category space and is asked a question.
   - If the space is a Camembert, a correct answer earns a camembert of that color.
   - The player who collects all 6 camemberts first wins.

## Project Structure

- `test.py` / `main.py`: Main entry point, runs the game loop.
- `jeu.py`: Contains the main game logic, player setup, turn management, and question handling.
- `plateau.py`: Manages the board, spaces, and their categories/types.
- `case.py`: Defines individual board spaces (category, position, type).
- `joueur.py`: Player class, tracks name, position, camemberts, and avatar.
- `question.py`: Question class, stores question text, choices, correct answer, and category.
- `utils.py`: Utility functions for console display, dice ASCII art, and color codes.
- `questions_trivial_pursuit.json`: JSON file with all questions, organized by category.

## Example Board

The board is visualized in the console with colored emojis representing categories and camemberts. Players' avatars are shown on their current position.

## Requirements

- Python 3.x
- No external dependencies (standard library only)

## How to Add Questions

Edit `questions_trivial_pursuit.json` to add or modify questions. Each category contains a list of questions, each with:
- `question`: The question text
- `reponses`: List of possible answers
- `bonne_reponse_index`: Index of the correct answer (starting from 0)
- `categorie`: (optional) The category name

Example:
```json
{
  "Python": [
    {
      "question": "Quel mot-clé permet de définir une fonction en Python ?",
      "reponses": ["def", "function", "lambda", "fun"],
      "bonne_reponse_index": 0
    }
  ]
}
```

## Customization

- You can change the categories, emojis, and board size in `plateau.py`.
- Modify the player setup or add more features in `jeu.py`.

## Authors

- Michael Adebayo ([@MichAdebayo](https://github.com/MichAdebayo))
- Hacene Zerrouk ([@haceneZERROUK](https://github.com/haceneZERROUK))
- Dorothée Catry ([@DorotheeCatry](https://github.com/DorotheeCatry))

# Hangman Game

This is a graphical Hangman game built using Python and Tkinter. Players guess letters to reveal a hidden word, with each incorrect guess bringing them closer to losing as the Hangman sketch is progressively drawn.

## Features

- A variety of **random secret words** from a predefined list.
- Displays **incorrect and correct letters** guessed by the player.
- Tracks the number of **tries remaining**.
- **Graphical representation** of the Hangman, updated after each incorrect guess.
- **Reset and Shuffle** buttons to restart or choose a new word during gameplay.
- Keyboard input support: Enter key for submitting guesses.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Musaddiq-Sultan/hangman-gui.git
    ```
   
2. Navigate to the project folder:
    ```bash
    cd hangman-gui
    ```

3. Install the required dependencies:
    ### Tkinter
   On Debain based Linux (Ubuntu/Mint/Deepin/Kali)
   ```bash
   sudo apt install python3-tk
   ```
   On Arch based Linux (EndeavourOS/Manjaro/Artix/Garuda)
   ```bash
   sudo pacman -Sy tk
   ```

5. Run the game:
    ```bash
    python main.py
    ```

## How to Play

1. Run the game and guess the secret word by entering one letter at a time in the input field.
2. The game tracks your correct and incorrect guesses, as well as the number of tries left.
3. The Hangman sketch updates with every incorrect guess.
4. **Win by guessing all the letters correctly**, or lose when the Hangman is fully drawn.

## Screenshots

![image](https://github.com/user-attachments/assets/73e9b3a1-a596-4a57-ae67-1ee8df70b02a)


## Future Improvements

- Adding more words to the list.
- Support for multiplayer mode.
- Adding difficulty levels based on the length of words.

## License

MIT License

Copyright (c) [2024] [Musaddiq Sultan]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


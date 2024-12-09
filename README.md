
# Quiz Game

A simple, interactive True/False quiz game built using Python. This program uses object-oriented programming principles to create a question model, manage quiz logic, and track the player's score.

## Table of Contents

- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## 📁 Project Structure

```
.
├── data.py             # Contains the list of questions with their categories, difficulties, and correct/incorrect answers.
├── main.py             # Entry point for the quiz game logic and user interaction.
├── question_model.py   # Defines the Question class to structure question objects.
├── quiz_brain.py       # Manages the logic of the quiz, tracks user progress, and checks answers.
```

---

## 🛠️ How It Works

1. **Data Setup**: The questions are defined in `data.py`, each containing the question text, correct answer, and incorrect answer(s).
2. **Object-Oriented Approach**: 
   - **`Question` Class**: Represents each question with its text and correct answer.
   - **`QuizBrain` Class**: Manages the quiz logic, tracks which question is currently being asked, checks the user's answer, and updates the score.
3. **Gameplay**: The game runs in a loop, asking users questions from the `question_bank` until there are no more questions left. The user's score is displayed at the end of the game.

---

## 📦 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/darrenlyl/Quiz-Brain.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd quiz brain
   ```

3. **Run the Quiz:**
   ```bash
   python main.py
   ```

---

## 🚀 Usage

1. **Run the Game**: 
   ```bash
   python main.py
   ```

2. **Answer the Questions**: The quiz will prompt you with True/False questions.
   - Type `True` or `False` to answer.
   - The program will provide feedback on whether your answer was correct or not.
   - Your final score is displayed at the end of the game.

---

## ✨ Features

- **Interactive Quiz**: Players can engage with an interactive True/False quiz.
- **Object-Oriented Design**: Uses classes and objects to organize logic and game flow.
- **Score Tracking**: Players receive immediate feedback on their answers and can see their final score at the end of the game.
- **Easy to Expand**: New questions can be added to `data.py` to extend the quiz.

---

## 🚀 Future Improvements

- **Randomized Question Order**: Shuffle the questions to provide a new experience on each playthrough.
- **Multiple Difficulty Levels**: Include difficulty levels such as "Easy", "Medium", and "Hard" to challenge players.
- **User Interface**: Upgrade the game with a graphical interface using libraries like `tkinter` or `pygame`.
- **Support for More Question Types**: Support multiple-choice and fill-in-the-blank questions.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions, improvements, or new ideas, please feel free to submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy the Quiz Game! 🚀

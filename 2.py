import tkinter as tk
import random

# Define the Maori words and their English translations
words = {
    "easy": {
        "kia ora": "hello",
        "whanau": "family",
        "kai": "food"
    },
    "medium": {
        "aroha": "love",
        "marae": "meeting house",
        "haka": "traditional dance"
    },
    "hard": {
        "whakapapa": "genealogy",
        "tino rangatiratanga": "self-determination",
        "kaitiakitanga": "guardianship"
    }
}

# Define the function to start the quiz
def start_quiz(level):
    # Get the words for the chosen level
    level_words = words[level]

    # Get the keys of the level words dictionary
    word_keys = list(level_words.keys())

    # Shuffle the keys
    random.shuffle(word_keys)

    # Initialize the score
    score = 0

    # Create the quiz window
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Maori Language Quiz - " + level)
    quiz_window.geometry("400x300")

    # Create the question label
    question_label = tk.Label(quiz_window, text="Translate the following Maori word:")
    question_label.pack(pady=10)

    # Create the score label
    score_label = tk.Label(quiz_window, text="Score: " + str(score))
    score_label.pack()

    # Create the answer entry
    answer_entry = tk.Entry(quiz_window)
    answer_entry.pack(pady=10)

    # Create the submit button
    def submit_answer():
        nonlocal score
        # Get the answer from the entry widget
        answer = answer_entry.get().lower()
        # Get the current word
        current_word = word_keys[len(word_keys) - 1]
        # Check the answer
        if answer == level_words[current_word]:
            score += 1
        # Remove the current word from the list of keys
        word_keys.pop()
        # Clear the entry widget
        answer_entry.delete(0, tk.END)
        # Update the score label
        score_label.config(text="Score: " + str(score))
        # If there are no more words, end the quiz
        if len(word_keys) == 0:
            quiz_window.destroy()
            end_label = tk.Label(root, text="Congratulations, you have finished the quiz with a score of " + str(score) + "!")
            end_label.pack(pady=10)

    submit_button = tk.Button(quiz_window, text="Submit", command=submit_answer)
    submit_button.pack()

    # Display the first word
    current_word = word_keys[len(word_keys) - 1]
    question_label.config(text="Translate the following Maori word: " + current_word)

# Create the main window
root = tk.Tk()
root.title("Maori Language Quiz")
root.geometry("400x300")

# Create the level buttons
easy_button = tk.Button(root, text="Easy", command=lambda: start_quiz("easy"))
easy_button.pack(pady=10)

medium_button = tk.Button(root, text="Medium", command=lambda: start_quiz("medium"))
medium_button.pack(pady=10)

hard_button = tk.Button(root, text="Hard", command=lambda: start_quiz("hard"))
hard_button.pack(pady=10)

# Run the main loop
root.mainloop()

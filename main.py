import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define the structure of your book
book_structure = {
    'Chapter 3': {
        '3.1': 50,
        '3.2': 45,
        '3.3': 40,
        '3.4': 35,
        # Add more sections as needed
    },
    # Add more chapters as needed
}

# Function to pick random problems
def pick_random_problems(book_structure):
    random_problems = {}
    for chapter, sections in book_structure.items():
        random_problems[chapter] = {}
        for section, num_problems in sections.items():
            random_problems[chapter][section] = random.randint(1, num_problems)
    return random_problems

# Function to save solved problems to a text file
def save_solved_problems(problems):
    with open("solved_problems.txt", "w") as file:
        for chapter, sections in problems.items():
            for section, problem in sections.items():
                file.write(f"{chapter},{section},{problem}\n")
    messagebox.showinfo("Saved", "Progress saved successfully!")

# Function to load previously solved problems from a text file
def load_solved_problems():
    solved_problems = {}
    try:
        with open("solved_problems.txt", "r") as file:
            for line in file:
                chapter, section, problem = line.strip().split(',')
                if chapter not in solved_problems:
                    solved_problems[chapter] = {}
                solved_problems[chapter][section] = int(problem)
    except FileNotFoundError:
        pass  # Handle if the file doesn't exist or is empty
    return solved_problems

# Create the Tkinter window
window = tk.Tk()
window.title("Random Problem Picker")

# Set the background color to metal gray
window.configure(bg='#808080')  # Replace with your desired shade of gray, e.g., #808080

# Define the size of the window
window.geometry("600x400")

# Load and display the wheel image
# Load and display the wheel image
wheel_image = Image.open("newton.jpg")  # Ensure you have a wheel.png image in the same directory
wheel_photo = ImageTk.PhotoImage(wheel_image)

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack(pady=20)
wheel_id = canvas.create_image(250, 250, image=wheel_photo)

# Function to pick random problems and display them
def spin_wheel():
    random_problems = pick_random_problems(book_structure)
    result_text = ""
    for chapter, sections in random_problems.items():
        result_text += f"{chapter}:\n"
        for section, problem in sections.items():
            result_text += f"  Section {section}: Problem {problem}\n"
    messagebox.showinfo("Random Problems", result_text)

# Create a button to spin the wheel
spin_button = tk.Button(window, text="Spin the Wheel", command=spin_wheel, bg='#C0C0C0')  # Adjust button color
spin_button.pack(pady=20)

# Function to handle saving progress when "Complete!" button is clicked
def complete():
    random_problems = pick_random_problems(book_structure)  # Generate random problems
    save_solved_problems(random_problems)  # Save the generated problems

# Create a "Complete!" button
complete_button = tk.Button(window, text="Complete!", command=complete, bg='#C0C0C0')
complete_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()

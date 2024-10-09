import tkinter as tk
from tkinter import PhotoImage
from os import path
import random

root = tk.Tk()
root.title("Hangman")
#root.resizable(0,0)
root.geometry("1250x700")
root.minsize(1006, 666)
root.configure(bg="#333")
root.grid_columnconfigure(0, weight=1, uniform="column")
root.grid_columnconfigure(1, weight=1, uniform="column")
root.grid_rowconfigure(0, weight=1)

secret_words = [
    "adventure", "balance", "blanket", "butterfly", "cactus", "carnival", "cereal", "chicken", "circus",
    "coffee", "compass", "concert", "cottage", "crystal", "cupcake", "diamond", "dolphin", "drizzle",
    "elephant", "explorer", "festival", "fireworks", "flamingo", "football", "fortune", "fountain", "galaxy",
    "garden", "giraffe", "goblin", "gorilla", "guitar", "hamburger", "hedgehog", "hiking", "honeycomb", "iceberg",
    "island", "jellyfish", "journey", "kangaroo", "koala", "laughter", "lighthouse", "lobster", "meadow",
    "mermaid", "moonlight", "mountain", "mushroom", "oatmeal", "octopus", "ostrich", "pancake", "panda",
    "parachute", "peacock", "penguin", "picnic", "pirate", "popcorn", "postcard", "pumpkin", "puzzle",
    "rainbow", "reindeer", "robot", "rocket", "scarecrow", "seashell", "shampoo", "snowflake", "spaceship",
    "squirrel", "strawberry", "sunflower", "sunshine", "surfboard", "telescope", "tentacle", "thunder", "tiger",
    "toothbrush", "toucan", "treasure", "trumpet", "tulip", "umbrella", "unicorn", "volcano", "waterfall",
    "whale", "wildflower", "windmill", "wizard", "yogurt", "zebra", "zeppelin", "zombie", "zookeeper", 
    "avocado", "balloon", "barnacle", "bicycle", "biscuit", "blizzard", "boomerang", "broccoli", "bubbles",
    "butterscotch", "carousel", "castle", "cheetah", "cherry", "chimney", "clover", "coconut", "comet", 
    "cornfield", "dandelion", "dinosaur", "dragonfly", "earthquake", "eggnog", "enchilada", "escalator",
    "feather", "fireplace", "fossil", "glacier", "goblet", "grapefruit", "hammock", "honeydew", "icecream",
    "igloo", "jigsaw", "jukebox", "kiwifruit", "ladder", "lasagna", "lawnmower", "licorice", "limousine",
    "lobster", "macaroni", "magician", "nachos", "nectarine", "noodles", "ostrich"]

secret_word = random.choice(secret_words).lower()
#secret_word = "aaaaabbbbbccccc".lower()
correct_letters = incorrect_letters = incorrect_letters_print = correct_letters_print = tried_letters = tried_letters_print = ""
tries = 8
cwd = path.dirname(__file__)
hangman_pics = [
    f"{cwd}/hangman_images/frame_00.png",
    f"{cwd}/hangman_images/frame_01.png",
    f"{cwd}/hangman_images/frame_02.png",
    f"{cwd}/hangman_images/frame_03.png",
    f"{cwd}/hangman_images/frame_04.png",
    f"{cwd}/hangman_images/frame_05.png",
    f"{cwd}/hangman_images/frame_06.png",
    f"{cwd}/hangman_images/frame_07.png",
    f"{cwd}/hangman_images/frame_08.png"]

def add_information_frame():
    global information_frame
    information_frame = tk.LabelFrame(root, text="Information" ,bg="#444", fg="#fff")
    information_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

def add_picture_frame():
    global picture_frame
    picture_frame = tk.LabelFrame(root, text="Sketch", bg="#444", fg="#fff")
    picture_frame.grid(row=0, column=1, sticky="nsew", padx=(0,5), pady=5)

def add_buttons_frame():
    global buttons_frame
    buttons_frame = tk.Frame(root, bg="#444")
    buttons_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=(0, 5))
    buttons_frame.columnconfigure(0, weight=1)
    buttons_frame.columnconfigure(1, weight=1)
    buttons_frame.grid_columnconfigure(2, weight=1)

def add_information_label():
    dashes_letters_label = tk.Label(information_frame, text=f"{dashes_letters()}", bg="#444", fg="#0ff", font=("", 20), justify="left")
    tries_label = tk.Label(information_frame, text=f"Tries Left: {tries}", bg="#444", fg="#37f", font=("", 20), justify="left")
    #tried_letters_label = tk.Label(information_frame, text=f"Tried Letters: {tried_letters_print}", bg="#444", fg="#37f", font=("", 20), justify="left")
    correct_letters_label = tk.Label(information_frame, text=f"Correct Letters: {correct_letters_print}", bg="#444", fg="#37f", font=("", 20), justify="left")
    incorrect_letters_label = tk.Label(information_frame, text=f"Incorrect Letters: {incorrect_letters_print}", bg="#444", fg="#37f", font=("", 20), justify="left")
    dashes_letters_label.grid(row=0, column=0, sticky="w",pady=(0, 50))
    tries_label.grid(row=1, column=0, sticky="w")
    #tried_letters_label.grid(row=2, column=0, sticky="w")
    correct_letters_label.grid(row=2, column=0, sticky="w")
    incorrect_letters_label.grid(row=3, column=0, sticky="w")

def add_hangman_picture_label():
    global hangman_picture_label, picture
    picture = PhotoImage(file=hangman_pics[-1*(tries + 1)])
    hangman_picture_label = tk.Label(picture_frame, image=picture, bg="#444")
    hangman_picture_label.grid(row=0, column=0, sticky="nsew")

def add_guess_label_entry():
    global guess_label, guess_entry
    guess_label = tk.Label(root, text="Enter Guess: ", bg="#444", fg="#fff", font=("", 20))
    guess_entry = tk.Entry(root, bg="#444", fg="#fff", insertbackground="#fff", highlightcolor="#fff", font=("", 20))
    guess_entry.bind("<Return>", submit)
    guess_label.grid(row=1, column=0, sticky="nsew", padx=(5), pady=5)
    guess_entry.grid(row=1, column=1, sticky="nsew", padx=(0,5), pady=5)

def add_buttons():
    global enter_button, reset_button
    enter_button = tk.Button(buttons_frame, bg="#444", fg="#fff", activebackground="#666", activeforeground="#fff", text="Enter", command=submit, font=("", 20))
    reset_button = tk.Button(buttons_frame, bg="#444", fg="#fff", activebackground="#666", activeforeground="#fff", text="Reset", command=reset, font=("", 20))
    shuffle_button = tk.Button(buttons_frame, bg="#444", fg="#fff", activebackground="#666", activeforeground="#fff", text="Shuffle", command=shuffle, font=("", 20))

    enter_button.grid(row=2, column=0, sticky="nsew", padx=(0,5), pady=5)
    reset_button.grid(row=2, column=1, sticky="nsew", pady=5)
    shuffle_button.grid(row=2, column=2, sticky="nsew", padx=(5,0), pady=5)

def delete_information_label():
    for widget in information_frame.winfo_children():
        widget.destroy()

def delete_hangman_picture_label():
    for widget in picture_frame.winfo_children():
        widget.destroy()

def clear_text_entry():
    guess_entry.delete(0, tk.END)

def clear_out():
    delete_information_label()
    delete_hangman_picture_label()
    #clear_text_entry()

def refresh_hangman():
    delete_hangman_picture_label()
    add_hangman_picture_label()

def refresh_info():
    delete_information_label()
    add_information_label()

def bind_enter_key():
    guess_entry.bind("<Return>", submit)

def unbind_enter_key():
    guess_entry.unbind("<Return>")

def dashes_letters():
    hidden_word = ""
    for letter in secret_word:
        if letter == " ":
            hidden_word += "-"
        elif letter in correct_letters:
            hidden_word += letter
        else:
            hidden_word += "_"
    return hidden_word

def calculate():
    global tried_letters, tried_letters_print, correct_letters, correct_letters_print, incorrect_letters, incorrect_letters_print, tries
    tried_letters += user_guess
    #tried_letters_print += user_guess + " "
    if user_guess in secret_word:
        correct_letters += user_guess * secret_word.count(user_guess)
        correct_letters_print += user_guess + " "
        tries += 1
    elif user_guess not in secret_word:
        incorrect_letters += user_guess
        incorrect_letters_print += user_guess + " "

def reset():
    global tries, user_guess, correct_letters, correct_letters_print, incorrect_letters, incorrect_letters_print, tried_letters, tried_letters_print
    correct_letters  = correct_letters_print = incorrect_letters = incorrect_letters_print = tried_letters = tried_letters_print = ""
    tries = 8
    clear_text_entry()
    refresh_hangman()
    refresh_info()
    if enter_button["state"] == "disabled":
        enter_button.config(state="normal")
    if guess_entry["state"] == "disabled":
        guess_entry.config(state="normal")
    guess_entry.bind("<Return>", submit)
    guess_entry.delete(0,"end")

def shuffle():
    global secret_word
    secret_word = random.choice(secret_words).lower()
    reset()

def submit(event=None):
    global tries, user_guess
    user_guess = guess_entry.get().lower()
    clear_out()
    delete_information_label()
    delete_hangman_picture_label()
    if len(user_guess.replace(" ", "")) != 1:
        tk.Label(information_frame, text="Please try a single letter", bg="#444", fg="#ff0", font=("", 20), justify="left").grid(row=4, column=0, pady=(50, 0), sticky="w")
        tries += 1
    elif user_guess in tried_letters:
        tk.Label(information_frame, text="Letter already tried", bg="#444", fg="#ff0", font=("", 20), justify="left").grid(row=4, column=0, pady=(50, 0), sticky="w")
        tries += 1
    else:
        calculate()

    tries -= 1

    if len(correct_letters.replace(" ", "")) == len(secret_word.replace(" ", "")):
        refresh_info()
        tk.Label(information_frame, text="You Win", bg="#444", fg="#0f0", font=("", 20), justify="left").grid(row=4, column=0, pady=(50, 0), sticky="w")
        enter_button.config(state="disabled")
        guess_entry.config(state="disabled")
        guess_entry.unbind("<Return>")
    elif tries <= 0:
        refresh_info()
        tk.Label(information_frame, text=f"You lose\nCorrect Word: {secret_word}", bg="#444", fg="#f33", font=("", 20), justify="left").grid(row=4, column=0, pady=(50, 0), sticky="w")
        enter_button.config(state="disabled")
        guess_entry.config(state="disabled")
        guess_entry.unbind("<Return>")

    add_information_label()
    add_hangman_picture_label()
    clear_text_entry()

add_information_frame()
add_picture_frame()
add_buttons_frame()
add_information_label()
add_hangman_picture_label()
add_guess_label_entry()
add_buttons()
bind_enter_key()

root.mainloop()
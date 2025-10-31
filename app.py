import tkinter as tk
from tkinter import messagebox, filedialog
import random
from main import background_task
import os
import threading
import sys



directory = os.path.expanduser('~')
folder_name = "Screenshots"
path = os.path.join(directory, folder_name)
hash_temp = None

current_path = [path]
stop_flag = threading.Event()


# Create window
root = tk.Tk()


if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, 'cat.ico')
else:
    icon_path = 'cat.ico'

try:
    root.iconbitmap(default=icon_path)
except:
    pass  
root.title("Purrfect Screenshot App 🐾")
root.geometry("420x320")
root.config(bg="mint cream")

# Greeting Label
greetings = [
    "Purr-fect to see you 😺",
    "Meow there! 🐱",
    "You look pawsome today 🐾",
    "Feeling fur-tastic? 🧶",
    "Let’s capture some clawsome shots! 📸"
]
label = tk.Label(root, text=random.choice(greetings), font=("Comic Sans MS", 14, "bold"), bg="mint cream", fg="dark slate gray")
label.pack(pady=15)

# Info Text
info_text = tk.Text(root, height=2, width=45, wrap="word", bg="lavender blush", fg="black", relief="flat")
info_text.insert(tk.END, "Please click below to choose your desired directory to store screenshots 🐾")
info_text.config(state="disabled")
info_text.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="No directory selected yet 😿", font=("Arial", 10, "italic"), bg="mint cream", fg="gray25")
status_label.pack(pady=5)

# Button click event
def choose_directory():
    if_directory = filedialog.askdirectory(title="Select Folder to Save Screenshots")
    if if_directory:
        current_path[0] = if_directory
        status_label.config(text=f"Directory chosen: {if_directory}", fg="green")
        # root.sel_dir = directory
    else:
        status_label.config(text="No directory selected 😿", fg="red")

    


# Fun message change
def surprise_me():
    label.config(text=random.choice(greetings))
    messagebox.showinfo("Meow!", "🐾 You made me happy!")

# Buttons Frame
button_frame = tk.Frame(root, bg="mint cream")
button_frame.pack(pady=10)

# Buttons
choose_btn = tk.Button(button_frame, text="🐾 Choose Directory", command=choose_directory, font=("Arial", 11, "bold"), bg="misty rose", fg="black", relief="ridge")
choose_btn.grid(row=0, column=0, padx=5)

surprise_btn = tk.Button(button_frame, text="😺 Surprise Me!", command=surprise_me, font=("Arial", 11, "bold"), bg="honeydew", fg="black", relief="ridge")
surprise_btn.grid(row=0, column=1, padx=5)

thread = threading.Thread(target=background_task, args=(current_path, hash_temp, stop_flag), daemon=True)
thread.start()


def on_close():
    stop_flag.set()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)



# Run app
root.mainloop()

# Import necessary modules
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *

# Define functions for various actions

# Function to change the text color
def change_color():
    color = colorchooser.askcolor(title="")
    text_area.config(fg=color[1])

# Function to change the font of the text
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

# Function to create a new file
def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

# Function to open an existing file
def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())

    except Exception:
        print("Couldn't read file")

    finally:
        file.close()

# Function to save the current text to a file
def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt") ])

    if not file:
        return

    try:
        window.title(os.path.basename(file))
        with open(file, "w") as file:
            file.write(text_area.get(1.0, END))
    except Exception as e:
        print("Couldn't save file:", e)

# Function to cut selected text
def cut():
    text_area.event_generate("<<Cut>>")

# Function to copy selected text
def copy():
    text_area.event_generate("<<Copy>>")

# Function to paste text from clipboard
def paste():
    text_area.event_generate("<<Paste>>")

# Function to display information about the program
def about():
    showinfo("About the program", "Practicing python")

# Function to quit the program
def quit():
    window.destroy

# Create the main window
window = Tk()
window.title("text editor")
file =  None

# Set window dimensions and position
window_width = 500
window_height = 500
screen_width = window.winfo_screenmmwidth()
screen_height = window.winfo_screenmmheight()

x = int((window_width / 2) - (screen_width / 2))
y = int((window_height / 2) - (screen_height/ 2))

window.geometry(f"{window_height}x{window_width}+{x}+{y}")

# Initialize variables for font and font size
font_name = StringVar(window)
font_name.set("Ariel")

font_size = StringVar(window)
font_size.set('25')

# Create the text area and scrollbar
text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

# Configure grid and layout for the text area
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

# Create a frame for buttons
frame = Frame(window)
frame.grid()

# Create buttons for changing text color, font, and size
color_button = Button(frame, text="Color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# Create a menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create menus for File, Edit, and Help
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Start the main event loop
window.mainloop()

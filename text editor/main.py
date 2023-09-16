import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="")
    text_area.config(fg=color[1])

def change_font():
    pass

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass

def quit():
    pass


window = Tk()

window.title("text editor")
file =  None

window_width = 500
window_height = 500
screen_width = window.winfo_screenmmwidth()
screen_height = window.winfo_screenmmheight()

x = int((window_width / 2) - (screen_width / 2))
y = int((window_height / 2) - (screen_height/ 2))

window.geometry(f"{window_height}x{window_width}+{x}+{y}")

font_name = StringVar(window)
font_name.set("Ariel")

font_size = StringVar(window)
font_size.set('25')

text_area = Text(window, font=(font_name.get(), font_size.get() ))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

window.mainloop()
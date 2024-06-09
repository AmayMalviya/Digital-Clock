import tkinter as tk
from tkinter import ttk
from time import strftime
from tkinter import colorchooser

# Function to update the time and date display
def update_time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%A, %B %d, %Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

# Function to change the background color
def change_bg_color():
    color = colorchooser.askcolor(title="Choose background color")[1]
    if color:
        root.config(bg=color)
        time_label.config(bg=color)
        date_label.config(bg=color)

# Function to change the foreground color
def change_fg_color():
    color = colorchooser.askcolor(title="Choose text color")[1]
    if color:
        time_label.config(fg=color)
        date_label.config(fg=color)

# Creating the main window
root = tk.Tk()
root.title('Digital Clock')

# Creating the time label
time_label = tk.Label(root, font=('calibri', 40, 'bold'), bg='purple', fg='white')
time_label.pack(anchor='center')

# Creating the date label
date_label = tk.Label(root, font=('calibri', 20), bg='purple', fg='white')
date_label.pack(anchor='center')

# Creating a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Adding a "Settings" menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Change Background Color", command=change_bg_color)
settings_menu.add_command(label="Change Text Color", command=change_fg_color)

# Start updating the time and date
update_time()

# Run the main loop
root.mainloop()

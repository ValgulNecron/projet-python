import tkinter as tk
from tkinter import messagebox

from client import Global


def account_info_ui(root):
    root.title("Informations du compte")
    root.resizable(width=False, height=False)

    # 8-bit style
    bg_color = "#444444"  # Background color
    fg_color = "#FFFFFF"  # Text color
    btn_color = "#FF9900"  # Button color
    font_style = ("Courier", 12, "bold")  # Font.
    # Create a frame for the content in the existing window
    frame = tk.Frame(root, bg=bg_color)  # Set the background color for the frame
    frame.pack()

    # Create the labels
    id_label = tk.Label(frame, text="ID: " + Global.ID)
    id_label.pack()

    root.mainloop()
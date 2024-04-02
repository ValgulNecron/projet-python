import tkinter as tk
from tkinter import messagebox

from client import Global
from client.src.client import GetAccount


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

    account = GetAccount.GetAccount(Global.ID, Global.TOKEN).get_account()
    # Create the labels
    id_label = tk.Label(frame, text="ID: " + Global.ID)
    id_label.pack()
    username_label = tk.Label(frame, text="Nom d'utilisateur")
    username_label.pack()
    username_entry = tk.Entry(frame)
    username_entry.insert(0, account['username'])
    username_entry.pack()
    email_label = tk.Label(frame, text="Email")
    email_label.pack()
    email_entry = tk.Entry(frame)
    email_entry.insert(0, account['email'])
    email_entry.pack()
    password_label = tk.Label(frame, text="Mot de passe")
    password_label.pack()
    password_entry = tk.Entry(frame)
    password_entry.pack()
    confirm_password_label = tk.Label(frame, text="Confirmer le mot de passe")
    confirm_password_label.pack()
    confirm_password_entry = tk.Entry(frame)
    confirm_password_entry.pack()

    root.mainloop()
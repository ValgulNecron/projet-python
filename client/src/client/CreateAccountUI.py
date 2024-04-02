import os
import tkinter as tk
from tkinter import messagebox
def signup_ui(root):
    # 8-bit style
    bg_color = "#444444"  # Background color
    fg_color = "#FFFFFF"  # Text color
    btn_color = "#FF9900"  # Button color
    font_style = ("Courier", 12, "bold")  # Font.
    # Create a frame for the content in the existing window
    frame = tk.Frame(root, bg=bg_color)  # Set the background color for the frame
    frame.pack()

    # Create the widgets with the 8-bit style
    username_label = tk.Label(frame, text="Nom d'utilisateur:", bg=bg_color, fg=fg_color, font=font_style)
    username_label.grid(row=0, column=0, sticky="w")
    username_entry = tk.Entry(frame, bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    username_entry.grid(row=0, column=1)
    password_label = tk.Label(frame, text="Mot de passe:", bg=bg_color, fg=fg_color, font=font_style)
    password_label.grid(row=1, column=0, sticky="w")
    password_entry = tk.Entry(frame, show="*", bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    password_entry.grid(row=1, column=1)
    confirm_password_label = tk.Label(frame, text="Confirmer le mot de passe:", bg=bg_color, fg=fg_color, font=font_style)
    confirm_password_label.grid(row=2, column=0, sticky="w")
    confirm_password_entry = tk.Entry(frame, show="*", bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    confirm_password_entry.grid(row=2, column=1)
    email_label = tk.Label(frame, text="Email:", bg=bg_color, fg=fg_color, font=font_style)
    email_label.grid(row=3, column=0, sticky="w")
    email_entry = tk.Entry(frame, bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    email_entry.grid(row=3, column=1)

    def create_account():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        email = email_entry.get()

        # Check if the fields are not empty
        if username.strip() == '' or password.strip() == '' or confirm_password.strip() == '' or email.strip() == '':
            messagebox.showerror("Erreur", "Tous les champs sont requis.")
        elif password != confirm_password:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")
        else:
            # Create an object CreateAccount
            import client.src.client.CreateAccount as CreateAccount
            CreateAccount.CreateAccount(email, password, username).create_account()

    create_button = tk.Button(frame, text="Créer le compte", bg=btn_color, fg=bg_color, font=font_style,
                              command=create_account)
    create_button.grid(row=4, column=1, columnspan=1)

    def login():
        frame.pack_forget()
        import client.src.client.LoginUI as CreateAccountUI
        CreateAccountUI.login_ui(root)

    login_button = tk.Button(frame, text="Se connecter", bg=btn_color, fg=bg_color, font=font_style,
                              command=login)
    login_button.grid(row=4, column=0, columnspan=1)


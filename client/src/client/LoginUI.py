import tkinter as tk
from tkinter import messagebox

from client.src.client.Login import Login


def login_ui(root):
    root.title("Connexion")
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
    username_label.grid(row=1, column=0, sticky="w")
    username_entry = tk.Entry(frame, bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    username_entry.grid(row=1, column=1)

    password_label = tk.Label(frame, text="Mot de passe:", bg=bg_color, fg=fg_color, font=font_style)
    password_label.grid(row=2, column=0, sticky="w")
    password_entry = tk.Entry(frame, show="*", bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    password_entry.grid(row=2, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Check if the fields are not empty
        if username.strip() == '' or password.strip() == '':
            messagebox.showerror("Erreur", "Tous les champs sont requis.")
        else:
            # Create a Login object
            try:
                Login(username, password).login()
                frame.pack_forget()  # Hide the current frame
                import client.src.client.AccountInfoUI as AccountInfoUI
                AccountInfoUI.account_info_ui(root)  # Call the account_info_ui function with the root window
            except Exception as e:
                messagebox.showerror("Erreur",
                                     "Erreur de connexion \nVeuillez vérifier votre connexion internet et votre mot de passe")
                frame.pack_forget()  # Hide the current frame
                login_ui(root)

    create_button = tk.Button(frame, text="Connexion", bg=btn_color, fg=bg_color, font=font_style,
                              command=login)
    create_button.grid(row=3, column=1, columnspan=1)

    def signup():
        frame.pack_forget()
        import client.src.client.CreateAccountUI as CreateAccountUI
        CreateAccountUI.signup_ui(root)

    signup_button = tk.Button(frame, text="Créer un compte", bg=btn_color, fg=bg_color, font=font_style,
                              command=signup)
    signup_button.grid(row=3, column=0, columnspan=1)

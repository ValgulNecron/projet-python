import tkinter as tk
from tkinter import messagebox

from client.src.client.Login import Login


def login():
    email = email_entry.get()
    password = password_entry.get()

    # Vérifier si les champs ne sont pas vides
    if email.strip() == '' or password.strip() == '':
        messagebox.showerror("Erreur", "Tous les champs sont requis.")
    else:
        # créer un objet Login
        login = Login(email, password)
        login.login()


# Créer la fenêtre principale
root = tk.Tk()
root.title("Connexion")

# Style 8-bit
bg_color = "#444444"  # Couleur de fond
fg_color = "#FFFFFF"  # Couleur du texte
btn_color = "#FF9900"  # Couleur du bouton
font_style = ("Courier", 12, "bold")  # Police de caractères

root.config(bg=bg_color)

# Créer les widgets avec le style 8-bit
email_label = tk.Label(root, text="Email:", bg=bg_color, fg=fg_color, font=font_style)
email_label.grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(root, bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
email_entry.grid(row=1, column=1)

password_label = tk.Label(root, text="Mot de passe:", bg=bg_color, fg=fg_color, font=font_style)
password_label.grid(row=2, column=0, sticky="w")
password_entry = tk.Entry(root, show="*", bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
password_entry.grid(row=2, column=1)

create_button = tk.Button(root, text="Connexion", bg=btn_color, fg=bg_color, font=font_style,
                          command=login)
create_button.grid(row=3, column=0, columnspan=2)

# Lancer la boucle principale
root.mainloop()

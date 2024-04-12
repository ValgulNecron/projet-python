import threading
import tkinter as tk
from tkinter import messagebox

from client import Global
from client.src.client import GetAccount


def account_info_ui(root):
    account = GetAccount.GetAccount(Global.ID, Global.TOKEN).get_account()
    root.title("Informations du compte")

    # 8-bit style
    bg_color = "#444444"  # Background color
    fg_color = "#FFFFFF"  # Text color
    btn_color = "#FF9900"  # Button color
    font_style = ("Courier", 12, "bold")  # Font.
    # Create a frame for the content in the existing window

    # create a label for the account (username, email, id, created_at, last_updated_at)
    # username, email and password are the only fields that can be updated
    frame = tk.Frame(root, bg=bg_color)
    frame.pack()

    username_label = tk.Label(frame, text="Nom d'utilisateur:", bg=bg_color, fg=fg_color, font=font_style)
    username_label.grid(row=1, column=0, sticky="w")
    username_entry = tk.Entry(frame, bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    username_entry.insert(0, account.username)
    username_entry.grid(row=1, column=1)

    email_label = tk.Label(frame, text="Email:", bg=bg_color, fg=fg_color, font=font_style)
    email_label.grid(row=2, column=0, sticky="w")
    email_entry = tk.Entry(frame, bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    email_entry.insert(0, account.email)
    email_entry.grid(row=2, column=1)

    id_label = tk.Label(frame, text="ID:", bg=bg_color, fg=fg_color, font=font_style)
    id_label.grid(row=3, column=0, sticky="w")
    id_value = tk.Label(frame, text=account.id, bg=bg_color, fg=fg_color, font=font_style)
    id_value.grid(row=3, column=1)

    created_label = tk.Label(frame, text="Créé le:", bg=bg_color, fg=fg_color, font=font_style)
    created_label.grid(row=4, column=0, sticky="w")
    created_value = tk.Label(frame, text=account.created, bg=bg_color, fg=fg_color, font=font_style)
    created_value.grid(row=4, column=1)

    last_updated_label = tk.Label(frame, text="Dernière mise à jour:", bg=bg_color, fg=fg_color, font=font_style)
    last_updated_label.grid(row=5, column=0, sticky="w")
    last_updated_value = tk.Label(frame, text=account.updated, bg=bg_color, fg=fg_color, font=font_style)
    last_updated_value.grid(row=5, column=1)

    password_label = tk.Label(frame, text="Mot de passe:", bg=bg_color, fg=fg_color, font=font_style)
    password_label.grid(row=6, column=0, sticky="w")
    password_entry = tk.Entry(frame, show="*", bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    password_entry.grid(row=6, column=1)

    confirm_password_label = tk.Label(frame, text="Confirmer le mot de passe:", bg=bg_color, fg=fg_color,
                                      font=font_style)
    confirm_password_label.grid(row=7, column=0, sticky="w")
    confirm_password_entry = tk.Entry(frame, show="*", bg=bg_color, fg=fg_color, font=font_style,
                                      insertbackground=fg_color)
    confirm_password_entry.grid(row=7, column=1)

    def update_account():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if username.strip() == '' or email.strip() == '' or password.strip() == '' or confirm_password.strip() == '':
            messagebox.showerror("Error", "All fields are required")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            try:
                import client.src.client.UpdateAccount as UpdateAccount
                UpdateAccount.UpdateAccount(Global.ID, Global.TOKEN, email, password, username).update_account()
                messagebox.showinfo("Information", "Account updated successfully")
                frame.pack_forget()
                account_info_ui(root)
            except Exception as e:
                messagebox.showerror("Error", "An error occurred: " + str(e))

    update_button = tk.Button(frame, text="Mettre à jour", bg=btn_color, fg=bg_color, font=font_style,
                              command=update_account)
    update_button.grid(row=8, column=0, columnspan=2)

    def delete_account():
        try:
            import client.src.client.DeleteAccount as DeleteAccount
            DeleteAccount.DeleteAccount(Global.ID, Global.TOKEN).delete_account()
            messagebox.showinfo("Information", "Account deleted successfully")
            frame.pack_forget()
            import client.src.client.ServerUI as ServerUI
            ServerUI.ask_for_server_address_ui(root)
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e))

    delete_button = tk.Button(frame, text="Supprimer le compte", bg=btn_color, fg=bg_color, font=font_style,
                              command=delete_account)
    delete_button.grid(row=9, column=0, columnspan=2)

    def logout():
        Global.ID = ""
        Global.TOKEN = ""
        frame.pack_forget()
        import client.src.client.LoginUI as LoginUI
        LoginUI.login_ui(root)

    logout_button = tk.Button(frame, text="Déconnexion", bg=btn_color, fg=bg_color, font=font_style,
                              command=logout)
    logout_button.grid(row=10, column=0, columnspan=2)

    def play():
        frame.pack_forget()
        root.title("")
        # launch the game
        print("Launching game")
        import client.src.map.map as GameUI
        GameUI.show_map(root)

    play_button = tk.Button(frame, text="Jouer", bg=btn_color, fg=bg_color, font=font_style,
                            command=play)
    play_button.grid(row=11, column=0, columnspan=2)

    root.mainloop()

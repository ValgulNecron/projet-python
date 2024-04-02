import os
import tkinter as tk
from tkinter import messagebox

from client import Global
def ask_for_server_address_ui():
    # Create the main window
    root = tk.Tk()
    root.title("Adresse du serveur")
    root.resizable(False, False)

    # 8-bit style
    bg_color = "#444444"  # Background color
    fg_color = "#FFFFFF"  # Text color
    btn_color = "#FF9900"  # Button color
    font_style = ("Courier", 12, "bold")  # Font

    root.config(bg=bg_color)

    # Create a frame for the content
    frame = tk.Frame(root, bg=bg_color)
    frame.pack()

    # Create the widgets with the 8-bit style
    # if the file exists, read the server address from it
    try:
        with open('server_address.txt', 'r') as file:
            server_address = file.read()
    except FileNotFoundError:
        server_address = ''

    server_address_label = tk.Label(frame, text="Adresse du serveur:", bg=bg_color, fg=fg_color, font=font_style)
    server_address_label.grid(row=1, column=0, sticky="w")
    server_address_entry = tk.Entry(frame, bg=bg_color, fg=fg_color, font=font_style, insertbackground=fg_color)
    server_address_entry.insert(0, server_address)
    server_address_entry.grid(row=1, column=1)

    def save_server_address():
        server_address = server_address_entry.get()
        if server_address.strip() == '':
            messagebox.showerror("Erreur", "L'adresse du serveur est requise.")
        else:
            with open('server_address.txt', 'w') as file:
                file.write(server_address)
            frame.pack_forget()  # Hide the current frame
            Global.IP = server_address
            import client.src.client.LoginUI as LoginUI
            LoginUI.login_ui(root)  # Call the login_ui function with the root window

    save_button = tk.Button(frame, text="Enregistrer", bg=btn_color, fg=bg_color, font=font_style,
                            command=save_server_address)
    save_button.grid(row=2, column=0, columnspan=2)

    # Start the main loop
    root.mainloop()


if __name__ == '__main__':
    for k in list(os.environ.keys()):
        if k.lower().endswith('_proxy'):
            del os.environ[k]
    ask_for_server_address_ui()
import os
import tkinter as tk

import client.src.client.ServerUI as UI

if __name__ == '__main__':
    for k in list(os.environ.keys()):
        if k.lower().endswith('_proxy'):
            del os.environ[k]
    root = tk.Tk()
    UI.ask_for_server_address_ui(root)

# main.py
import tkinter as tk
from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import GarajeApp

if __name__ == "__main__":
    root = tk.Tk()
    servicio = GarajeServicio()
    app = GarajeApp(root, servicio)
    root.mainloop()
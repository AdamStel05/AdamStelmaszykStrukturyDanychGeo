import tkinter as tk
from tkinter import filedialog

from src.data_service import get_layer
from src.data_service import set_layer

def coordinate_system():
    layer = get_layer()

    if layer is None:
        return

    window = tk.Toplevel()
    window.title("Zmień układ współrzędnych")
    window.geometry("400x300")

    current_crs = f"EPSG:{layer.crs.to_epsg()} ({layer.crs.name})"
    tk.Label(window, text=f"Obecny układ: {current_crs}").pack()

    new_crs_var = tk.StringVar()

    tk.Label(window, text="Cyfry nowego układu współrzędnych:").pack()
    tk.Entry(window, textvariable=new_crs_var).pack()

    def apply_crs():
        target_crs = f"EPSG:{new_crs_var.get().strip()}"
        transformed_layer = layer.to_crs(target_crs)
        set_layer(transformed_layer)

    tk.Button(
        window,
        text="Zmień",
        command=apply_crs
    ).pack()
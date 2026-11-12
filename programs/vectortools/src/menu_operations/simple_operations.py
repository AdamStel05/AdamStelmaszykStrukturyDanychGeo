import tkinter as tk
from tkinter import filedialog

from src.data_service import get_layer

def simple_operations():
    layer = get_layer()

    if layer is None:
        return

    window = tk.Toplevel()
    window.title("Proste operacje")
    window.geometry("400x300")

    operation = tk.StringVar(value="buffer")
    threshold = tk.StringVar()

    tk.Label(window, text="Operacja:").pack()

    tk.OptionMenu(
        window,
        operation,
        "buffer",
        "convex hull",
        "simplify",
        "centroid"
    ).pack()

    limit_frame = tk.Frame(window)
    limit_label = tk.Label(limit_frame, text="Limit (odległość bufora):")
    limit_label.pack()
    limit_entry = tk.Entry(limit_frame, textvariable=threshold)
    limit_entry.pack()

    def update_limit_visibility(*args):
        op = operation.get()
        if op in ("buffer", "simplify"):
            if op == "buffer":
                limit_label.config(text="Limit (odległość bufora):")
            else:
                limit_label.config(text="Limit (tolerancja upraszczania):")
            limit_frame.pack(pady=10, before=execute_btn)
        else:
            limit_frame.pack_forget()
            threshold.set("")

    def execute():

        result = layer.copy()
        
        if operation.get() == "buffer":
            value = float(threshold.get())
            result["geometry"] = layer.geometry.buffer(value)

        elif operation.get() == "convex hull":
            result["geometry"] = layer.geometry.convex_hull

        elif operation.get() == "simplify":
            value = float(threshold.get())
            result["geometry"] = layer.geometry.simplify(value)

        elif operation.get() == "centroid":
            result["geometry"] = layer.geometry.centroid

        path = filedialog.asksaveasfilename(
            defaultextension=".geojson",
            filetypes=[("GeoJSON", "*.geojson")]
        )

        if path:
            result.to_file(path)
            window.destroy()

    execute_btn = tk.Button(
        window,
        text="Wykonaj",
        command=execute
    )
    execute_btn.pack()

    operation.trace_add("write", update_limit_visibility)
    update_limit_visibility()
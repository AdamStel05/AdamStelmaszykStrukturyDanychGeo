import tkinter as tk
from PIL import Image, ImageTk

canvas.create_text(
    150,
    500,
    text="Wyjdź",
    font=("Times New Roman", 20, "italic"),
    fill="black",
    tags="zamknij"
)

canvas.tag_bind(
    "zamknij",
    "<Button-1>",
    lambda event: close_program()
)

canvas.tag_bind(
    "zamknij",
    "<Enter>",
    lambda event: canvas.itemconfig(
        "zamknij",
        fill="#FF0000"
    )
)

canvas.tag_bind(
    "zamknij",
    "<Leave>",
    lambda event: canvas.itemconfig(
        "zamknij",
        fill="black"
    )
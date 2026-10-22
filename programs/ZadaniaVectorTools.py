import tkinter as tk
from PIL import Image, ImageTk

def close_program():
    window.destroy()

window = tk.Tk()
window.title("Wielka strona")
window.resizable(False, False)

canvas = tk.Canvas(
    window,
    width=1920,
    height=1280,
    highlightthickness=0
)

canvas.pack()

pil_image = Image.open("lew.png")
background_screen = ImageTk.PhotoImage(pil_image)

canvas.create_image(
    0,
    0,
    image=background_screen,
    anchor="nw"
)

canvas.create_text(
    350,
    100,
    text="Wielka strona z lwem",
    font=("Times New Roman", 60, "italic"),
    fill="black"
)

canvas.create_text(
    150,
    400,
    text="Opcje",
    font=("Times New Roman", 30, "italic"),
    fill="black"
)

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
)

window.mainloop()
import tkinter as tk
from PIL import Image, ImageTk

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
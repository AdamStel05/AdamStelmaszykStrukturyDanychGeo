import tkinter as tk

def close_program():
    window.destroy()

window = tk.Tk()
window.title("Wielka strona")
window.resizable(False, False)

canvas = tk.Canvas(
    window,
    width=700,
    height=700,
    highlightthickness=0
)

canvas.pack()

background_screen = tk.PhotoImage(file="lew.png")

canvas.create_image(
    0,
    0,
    image=background_screen,
    anchor="nw"
)

canvas.create_text(
    300,
    100,
    text="Wielka strona",
    font=("Times New Roman", 30, "italic"),
    fill="white"
)


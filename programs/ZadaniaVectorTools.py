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

background_screen = tk.PhotoImage(file="C:/Users/stelm/Downloads/Piąty semestr/lew.png")

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
    fill="black"
)

canvas.create_text(
    150,
    400,
    text="Opcje:",
    font=("Times New Roman", 15, "italic"),
    fill="black"
)

canvas.create_text(
    150,
    400,
    text="Wyjdź",
    font=("Times New Roman", 10, "italic"),
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
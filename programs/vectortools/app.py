from src.create_window import create_window
from src.create_menu_option import create_menu_option
from src.update_menu import update_menu
from src.menu_operations.close_program import close_program
from src.menu_operations.load_data import load_data_and_remember_outcome
from src.menu_operations.show_layer import show_layer
from src.menu_operations.show_layer_info import show_layer_info
from src.menu_operations.save_data import save_data
from src.menu_operations.coordinate_system import coordinate_system
from src.menu_operations.simple_operations import simple_operations

window, canvas = create_window()
zaladowany = False
wysokosc = 350

def on_load_data():
    global zaladowany
    data = load_data_and_remember_outcome()
    update_menu(canvas)
    if data and not zaladowany:
        show_remaining_options()
        zaladowany = True

def show_remaining_options():
    opcje = (
        ("Wyświetlenie warstwy", show_layer),
        ("Informacje o warstwie", show_layer_info),
        ("Zapisanie warstwy", save_data),
        ("Zmiana układu wsp.", coordinate_system),
        ("Proste operacje", simple_operations),
        ("Wyjdź", lambda: close_program(window))
    )
    for x, (tekst, akcja) in enumerate(opcje, start = 1):
        create_menu_option(canvas, wysokosc + (50 * x), tekst, akcja)

create_menu_option(canvas, wysokosc, "Wczytanie warstwy", on_load_data)
window.mainloop()
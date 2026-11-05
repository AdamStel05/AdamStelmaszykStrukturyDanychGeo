from src.create_window import create_window
from src.create_menu_option import create_menu_option
from src.update_menu import update_menu
from src.menu_operations.close_program import close_program
from src.menu_operations.load_data import load_data_and_remember_outcome
from src.menu_operations.show_layer import show_layer
from src.menu_operations.show_layer_info import show_layer_info
from src.menu_operations.save_data import save_data
from src.menu_operations.simple_operations import simple_operations

window, canvas = create_window()

create_menu_option(canvas, 350, "Wczytanie warstwy", lambda: load_data_and_remember_outcome(), lambda: update_menu())
create_menu_option(canvas, 400, "Wyświetlenie warstwy", lambda: show_layer())
create_menu_option(canvas, 450, "Informacje o warstwie", lambda: show_layer_info())
create_menu_option(canvas, 500, "Zapisanie warstwy", lambda: save_data())
create_menu_option(canvas, 550, "Proste operacje", lambda: simple_operations())
create_menu_option(canvas, 600, "Wyjdź", lambda: close_program(window))

window.mainloop()
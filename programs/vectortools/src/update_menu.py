from src.data_service import get_layer

def update_menu(canvas):
    canvas.delete("layer_status")

    if get_layer() is not None:
        canvas.create_text(
            200,
            300,
            text="Plik załadowano poprawnie",
            fill="green",
            tags="layer_status"
        )
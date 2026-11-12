from src.data_service import get_layer

def update_menu(canvas):
    canvas.delete("layer_status")

    if get_layer() is not None:
        canvas.create_text(
            150,
            300,
            text="Plik załadowano poprawnie",
            fill="green",
            tags="layer_status"
        )
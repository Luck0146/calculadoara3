import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, BOLD


def build(app):
    # Asignar el tamaño compacto de la ventana
    app.main_window.size = (330, 450)

    # Variables de estado
    expresion = [""]

    # Contenedor principal con el tono más fuerte (#5C6BC0)
    main_box = toga.Box(
        style=Pack(
            direction=COLUMN,
            padding=15,
            background_color="#5C6BC0"
        )
    )

    # Display / Pantalla (#E8EAF6)
    display = toga.TextInput(
        readonly=True,
        style=Pack(
            padding=10,
            font_size=22,
            font_weight=BOLD,
            text_align=CENTER,
            background_color="#E8EAF6",
            color="#5C6BC0"
        )
    )
    main_box.add(display)

    # Lógica de los botones
    def presionar_boton(widget):
        texto = widget.text
        if texto == "C":
            expresion[0] = ""
        elif texto == "=":
            try:
                resultado = eval(expresion[0])
                if isinstance(resultado, float) and resultado.is_integer():
                    resultado = int(resultado)
                expresion[0] = str(resultado)
            except Exception:
                expresion[0] = "Error"
        else:
            if expresion[0] == "Error":
                expresion[0] = ""
            expresion[0] += texto

        display.value = expresion[0]

    # Distribución de botones
    botones_grid = [
        ["C", "(", ")", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "="]
    ]

    # Generar botones con la paleta de colores
    for fila in botones_grid:
        fila_box = toga.Box(style=Pack(direction=ROW, padding=3))
        for item in fila:
            es_operador = item in ["C", "(", ")", "/", "*", "-", "+", "="]
            
            color_fondo = "#7986CB" if es_operador else "#C5CAE9"
            color_texto = "#FFFFFF" if es_operador else "#5C6BC0"

            btn = toga.Button(
                item,
                on_press=presionar_boton,
                style=Pack(
                    flex=1,
                    height=50,
                    padding=3,
                    font_size=16,
                    font_weight=BOLD,
                    background_color=color_fondo,
                    color=color_texto
                )
            )
            fila_box.add(btn)
        main_box.add(fila_box)

    # Función para mostrar el diálogo con los datos solicitados
    def mostrar_informacion(widget):
        app.main_window.info_dialog(
            "Información",
            "Librería: Toga\nAutor: Jaquelin Cielo V."
        )

    # Crear un grupo de menú personalizado visible
    grupo_opciones = toga.Group("Opciones")

    # Comando "Información" agregado al grupo personalizado
    cmd_info = toga.Command(
        mostrar_informacion,
        text="Información",
        group=grupo_opciones
    )
    
    # Agregar el comando a la lista de comandos globales de la app
    app.commands.add(cmd_info)

    return main_box


def main():
    return toga.App("Calculadora", "org.beeware.toga.calculadora", startup=build)


if __name__ == "__main__":
    main().main_loop()
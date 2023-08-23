from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()

    font_list = figlet.getFonts()
    print("Fuentes disponibles:")
    for font in font_list:
        print(font)

    selected_font = input("Ingrese el nombre de la fuente (deje en blanco para aleatoria): ")
    if not selected_font:
        selected_font = random.choice(font_list)

    user_text = input("Ingrese el texto a imprimir: ")

    try:
        figlet.setFont(font=selected_font)
        rendered_text = figlet.renderText(user_text)
        print(rendered_text)
    except ValueError:
        print("Fuente no válida.")

if __name__ == "__main__":
    main()

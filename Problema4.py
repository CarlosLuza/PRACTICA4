class Multiplicar:
    def save_multiplication_table(self, num):
        if num < 1 or num > 10:
            print("El número debe estar entre 1 y 10.")
            return

        filename = f"tabla-{num}.txt"
        with open(filename, "w") as file:
            for i in range(1, 11):
                line = f"{num} x {i} = {num * i}\n"
                file.write(line)
        print(f"Tabla de multiplicar de {num} guardada en {filename}")

    def read_whole_table(self, num):
        try:
            filename = f"tabla-{num}.txt"
            with open(filename, "r") as file:
                table_content = file.read()
                print(table_content)
        except FileNotFoundError:
            print(f"El archivo {filename} no existe.")

    def read_specific_line(self, num, line_num):
        try:
            filename = f"tabla-{num}.txt"
            with open(filename, "r") as file:
                lines = file.readlines()
                if 1 <= line_num <= len(lines):
                    print(lines[line_num - 1].strip())
                else:
                    print(f"La línea {line_num} no existe en el archivo.")
        except FileNotFoundError:
            print(f"El archivo {filename} no existe.")

def main():
    manager = Multiplicar()

    while True:
        print("\n1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla completa")
        print("3. Mostrar línea específica")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            num = int(input("Ingrese un número entre 1 y 10: "))
            manager.save_multiplication_table(num)
        elif choice == "2":
            num = int(input("Ingrese un número entre 1 y 10: "))
            manager.read_whole_table(num)
        elif choice == "3":
            num = int(input("Ingrese un número entre 1 y 10: "))
            line_num = int(input("Ingrese el número de línea a mostrar: "))
            manager.read_specific_line(num, line_num)
        elif choice == "4":
            print("¡Hasta luego!, vuela pronto")
            break
        else:
            print("Opción inválida. Reintente.")

if __name__ == "__main__":
    main()


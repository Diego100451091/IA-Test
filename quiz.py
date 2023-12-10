import getpass

from constants import COLORS
from utils import clear_terminal
from studyMode import study_mode
from guessMode import guess_mode
from IO import read_json_file, delete_file
from settings import settings_mode, get_questions

def main():
    while True:
        clear_terminal()
        print(
            f"{COLORS['purple']}==========| MODO DE JUEGO |=========={COLORS['reset']}")
        print("Seleccione el modo de juego: ")
        print("1. Modo estudio")
        print("2. Modo test")
        print("3. Modo errores")
        print("4. Eliminar registro errores")
        print("5. Ajustes")
        print("6. Salir")
        option = input("\nOpcion: ")
        if (option == "1"):
            study_mode(get_questions())
        elif (option == "2"):
            guess_mode(get_questions())
        elif (option == "3"):
            wrong_dict = read_json_file("wrong_questions.json")
            if (wrong_dict != None):
                guess_mode(wrong_dict)
            else:
                print("No hay registro de palabras falladas")
                getpass.getpass("Pulsa ENTER para continuar.")
        elif (option == "4"):
            delete_file("wrong_questions.json")
            print("Registro de errores eliminado")
            getpass.getpass("Pulsa ENTER para continuar.")
        elif (option == "5"):
            settings_mode()
        elif (option == "6"):
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
            getpass.getpass("Pulsa ENTER para continuar.")

if __name__ == "__main__":
    main()

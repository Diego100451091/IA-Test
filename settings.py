import getpass
from IO import read_json_file, write_json_file
from utils import clear_terminal
from terminalPrints import print_title, print_text_with_bg

def get_questions():
    settings = get_settings()
    questions = []
    all_questions = read_json_file("dictionary.json")
    for setting in settings:
        if (settings[setting] == 1):
            # Add the list to the questions list
            questions += all_questions[setting]
    
    return questions

def get_settings():
    settingsSchema = {
        "AutoML": 1,
        "Vehículos Autónomos": 1,
        "IA en Medicina": 1,
        "IA & Música": 1,
        "IA & Robótica": 1,
        "Inteligencia de Enjambre": 1,
        "Deepfakes": 1,
        "Generacion de código": 1
    }
    previous_settings = read_json_file("settings.json")
    if (read_json_file("settings.json") != None):
        settings = previous_settings
        for key in settingsSchema:
            if key not in previous_settings:
                settings[key] = settingsSchema[key]
    else:
        settings = settingsSchema
    return settings


def settings_mode():
    settings = get_settings()

    while True:
        clear_terminal()
        print_title("SELECCIONE LOS TEMAS A UTILIZAR")
        print("1. AutoML:", end="  ")
        printStatus(settings["AutoML"] == 1)
        print("2. Vehículos Autónomos:", end= "  ")
        printStatus(settings["Vehículos Autónomos"] == 1)
        print("3. IA en Medicina:", end= "  ")
        printStatus(settings["IA en Medicina"] == 1)
        print("4. IA & Música:", end= "  ")
        printStatus(settings["IA & Música"] == 1)
        print("5. IA & Robótica:", end= "  ")
        printStatus(settings["IA & Robótica"] == 1)
        print("6. Inteligencia de Enjambre:", end= "  ")
        printStatus(settings["Inteligencia de Enjambre"] == 1)
        print("7. Deepfakes:", end= "  ")
        printStatus(settings["Deepfakes"] == 1)
        print("8. Generacion de código:", end= "  ")
        printStatus(settings["Generacion de código"] == 1)
        print("9. Salir y guardar los cambios")
        option = input("\nOpcion: ")
        if (option == "1"):
            settings["AutoML"] = abs(settings["AutoML"]-1)
        elif (option == "2"):
            settings["Vehículos Autónomos"] = abs(settings["Vehículos Autónomos"]-1)
        elif (option == "3"):
            settings["IA en Medicina"] = abs(settings["IA en Medicina"]-1)
        elif (option == "4"):
            settings["IA & Música"] = abs(settings["IA & Música"]-1)
        elif (option == "5"):
            settings["IA & Robótica"] = abs(settings["IA & Robótica"]-1)
        elif (option == "6"):
            settings["Inteligencia de Enjambre"] = abs(settings["Inteligencia de Enjambre"]-1)
        elif (option == "7"):
            settings["Deepfakes"] = abs(settings["Deepfakes"]-1)
        elif (option == "8"):
            settings["Generacion de código"] = abs(settings["Generacion de código"]-1)
        elif (option == "9"):
            write_json_file("settings.json", settings)
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
            getpass.getpass("Pulsa ENTER para continuar.");


def printStatus(active, activatedString="Activado", desactivatedString="Desactivado"):
    if (active):
        print_text_with_bg(activatedString, "cyan", end="  ")
        print(desactivatedString)
    else:
        print(activatedString, end="  ")
        print_text_with_bg(desactivatedString, "cyan")


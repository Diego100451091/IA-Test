import sys
import random
from utils import clear_terminal, get_exit, print_question
from terminalPrints import print_title, print_colored_text, print_progress
from IO import write_json_file
from settings import get_settings


def guess_mode(questions):
    remaining_questions = questions.copy()
    wrong_questions = []
    
    status_vector = []
    total_questions_lenght = len(questions)
    for i in range(total_questions_lenght):
        status_vector.append(0)
    status_index = 0

    while True:
        clear_terminal()
        print_title("MODO TEST")

        print_progress(status_vector)

        if (len(remaining_questions) == 0):
            print("Ya se han mostrado todas las palabras")
            break

        question = remaining_questions.pop(random.randrange(len(remaining_questions)))
        print_question(question)

        answer = get_user_answer()

        if (answer == question["answer"]):
            print_colored_text("¡Correcto!", "green")
            status_vector[status_index] = 1
        else:
            print_colored_text("Incorrecto", "red", "")
            print(" - La opción correcta era: ", question["answer"])
            status_vector[status_index] = -1
            wrong_questions.append(question)

        status_index += 1

        if get_exit():
            break

    show_wrong_questions(wrong_questions)
    write_json_file("wrong_questions.json", wrong_questions)

def get_user_answer():
    while True:
        answer = input("_\r")
        if (answer in ["a", "b", "c", "d"]):
            return answer
        # Go one line up and remove the line
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.flush()


def show_wrong_questions(wrong_questions):
    print("\nPalabras falladas:")
    for question in wrong_questions:
        print_question(question)
        print("Respuesta: ", question["answer"],"\n")

    get_exit()


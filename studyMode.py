import random
from utils import clear_terminal, get_exit, print_question
from terminalPrints import print_title, print_progress

def study_mode(dictionary):
    remaining_questions = dictionary.copy()

    status_vector = []
    total_dictionary_lenght = len(dictionary)
    for i in range(total_dictionary_lenght):
        status_vector.append(0)
    status_index = 0

    while True:
        clear_terminal()
        print_title("MODO ESTUDIO")

        print_progress(status_vector)
        
        if (len(remaining_questions) == 0):
            print("Ya se han mostrado todas las palabras")
            break

        question = remaining_questions.pop(random.randrange(len(remaining_questions)))
        print_question(question)
        print("Respuesta: ", question["answer"])

        status_vector[status_index] = 1
        status_index += 1
        
        if get_exit():
            break


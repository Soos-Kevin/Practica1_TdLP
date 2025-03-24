import random

# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero enPython?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
("// Esto es un comentario","/* Esto es un comentario */","-- Esto es un comentario","# Esto es un comentario"),
("=", "==", "!=", "===")
]

# Índice de la respuesta correcta para cada pregunta, es el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

user_score = 0

#Se crea una lista con las preguntas aleatorias sin repetir
questions_to_ask = random.sample(list(zip(questions,
answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for i in range(3):

    #Guardo la posición de la respuesta correcta
    correct_answer = questions_to_ask[i][2]

    # Se muestra la pregunta y las respuestas posibles
    print(questions_to_ask[i][0])
    for a, answer in enumerate(questions_to_ask[i][1]):
        print(f"{a + 1}. {answer}")

    # El usuario tiene 2 intentos para respondercorrectamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica que la respuesta sea un numero y este entre 1 y 4
        if (user_answer.isnumeric() and 0<int(user_answer)<=4):
            user_answer = int(user_answer) - 1
            # Se verifica si la respuesta es correcta  
            if user_answer == correct_answer:
                print("¡Correcto!")
                user_score += 1
                break
            else:
                user_score -=0.5
        else:
            print("Respuesta no valida")
            exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(questions_to_ask[i][1][correct_answer])
        # Se imprime un blanco al final de la pregunta
        print()
    print()
#Muestro los puntajes
if user_score <= 0:
    print("Puntaje: 0")
else:
    print(f"Puntaje: {user_score}")
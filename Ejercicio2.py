
import random as randind
from colorama import init, Fore, Back, Style

mensajes_motivacionales = [
    "No tienes que ser el mejor, solo dar lo mejor de ti.",
    "Cada paso, por pequeño que sea, te acerca a donde quieres estar.",
    "Hoy es un buen día para empezar algo nuevo.",
    "El éxito es la suma de pequeños esfuerzos repetidos cada día.",
    "Confía en el proceso, incluso cuando no veas resultados inmediatos.",
    "Eres más fuerte de lo que crees y más capaz de lo que imaginas.",
    "Las dificultades son oportunidades disfrazadas.",
    "Hazlo con miedo, pero hazlo.",
    "Lo importante no es cuántas veces caes, sino cuántas te levantas.",
    "Tu futuro lo construyes hoy.",
    "Espero que tu día esté lleno de pequeñas alegrías.",
    "No olvides cuidar de ti tanto como cuidas de los demás.",
    "Me alegra saber que existes.",
    "Un pequeño mensaje para recordarte lo genial que eres.",
    "Las personas como tú hacen del mundo un lugar mejor.",
    "Hoy puede ser un gran día, todo depende de tu actitud.",
    "Gracias por ser tú. El mundo necesita más personas así.",
    "Recuerda sonreír, alguien puede necesitar esa luz hoy.",
    "Tómate un momento para respirar… estás haciendo un gran trabajo."
]

nombres = ["Juan","María","Pedro","Ana","Luis","Laura","Carlos","Sofía","Javier","Isabel"]

def menu():
    while True:
        Print_mensaje = "ver un mensaje"
        Print_lista = "mostrar una lista de nombres"
        Print_salir = "salir del programa"
        
        print("------------------------------------------------------------------------------------------")
        print("Menú Interactivo")
        print(Fore.MAGENTA + "1. " + Print_mensaje + Fore.RESET)
        print(Fore.MAGENTA + "2. " + Print_lista + Fore.RESET)
        print(Fore.MAGENTA + "3. " + Print_salir + Fore.RESET)
        print("------------------------------------------------------------------------------------------")

        
        opcion = input("Seleccione una opción (1-3): ")
        print("")
        
        
        if opcion == "1" or opcion in Print_mensaje:
            print("------------------------------------------------------------------------------------------")
            print(Fore.YELLOW + "" + randind.choice(mensajes_motivacionales) + Fore.RESET)
            print("------------------------------------------------------------------------------------------")
            print("")
            
        elif opcion == "2" or opcion in Print_lista:
            print(Fore.GREEN + "", nombres, Fore.RESET)
            print("")
    
        elif opcion == "3" or opcion in Print_salir:
            print(Fore.CYAN + "Gracias por usar el programa. ¡Hasta luego!" + Fore.RESET)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            print("")
            
menu()
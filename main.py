from datetime import datetime
from ohce import echo, saludo

def main():
    nombre = input("¿Cuál es tu nombre? ")
    hora = datetime.now()
    
    # Saludo inicial
    print(saludo(nombre, hora))

    while True:
        entrada = input(">")
        salida = echo(entrada, nombre)
        print(salida)
        
        if entrada == "Stop!":
            break
if __name__ == "__main__":
    main()
from datetime import datetime

def echo(text, name=""):
    if text == "Stop!":
        return f"Adios {name}"
    reversed_text = text[::-1]
    if text == reversed_text:
        return f"{reversed_text}\n¡Bonita palabra!"
    return reversed_text

def saludo(name, hora):
    if 6 <= hora.hour < 12:
        return f"¡Buenos días {name}!"
    elif 12 <= hora.hour < 20:
        return f"¡Buenas tardes {name}!"
    else:
        return f"¡Buenas noches {name}!"

def run_ohce(nombre, hora=None):
    if hora is None:
        hora = datetime.now()
    return saludo(nombre, hora)

def ohce_loop(nombre, entradas, hora=None):
    return f"Buenos días {nombre}!" if hora is None else run_ohce(nombre, hora)
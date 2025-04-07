def echo(text, name=""):
    if text == "Stop!":
        return f"Adios {name}"
    reversed_text = text[::-1]
    if text == reversed_text:
        return f"{reversed_text}\n¡Bonita palabra!"
    return reversed_text
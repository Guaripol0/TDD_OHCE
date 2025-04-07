def echo(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        return f"{reversed_text}\n¡Bonita palabra!"
    return reversed_text
# TDD_OHCE

Tarea 1 Fundamentos de testing y aseguramiento de calidad

Implementación del algoritmo ohce que sigue la siguiente estructura de una conversación:
¿Cuál es tu nombre? Pedro
¡Buenas tardes Pedro!

> madam
> madam
> ¡Bonita palabra!
> hello
> olleh
> Stop!
> Adios Pedro

Donde se implementan las siguientes funcionalidades:

- Invierte cualquier palabra ingresada.
- Detecta palíndromos y responde con “¡Bonita palabra!”.
- Se despide cuando el usuario escribe `Stop!`.
- Saluda al usuario según la hora del sistema:
  - `6:00 – 11:59` → ¡Buenos días {nombre}!
  - `12:00 – 19:59` → ¡Buenas tardes {nombre}!
  - `20:00 – 5:59` → ¡Buenas noches {nombre}!

## Instalación

Para la instalación se requiere python 3.12 y ejecutar el siguiente comando

pip install -r requirements.txt

## Tests

Los tests están escritos con pytest. Para ejecularlos usar el comando: pytest

Los tests cubren:
-Reverso de palabras
-Palíndromos
-Saludo según hora
-Salida al ingresar Stop!
-Flujo lógico completo con entradas simuladas

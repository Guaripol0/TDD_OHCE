from datetime import datetime
import ohce

def test_echo_reversed_word():
    assert ohce.echo("hello") == "olleh"
    assert ohce.echo("world") == "dlrow"
    assert ohce.echo("python") == "nohtyp"

def test_echo_palindrome_word():
    assert ohce.echo("madam") == "madam\n¡Bonita palabra!"
    assert ohce.echo("racecar") == "racecar\n¡Bonita palabra!"
    assert ohce.echo("level") == "level\n¡Bonita palabra!"

def test_stop_returns_goodbye():
    assert ohce.echo("Stop!", name="Pedro") == "Adios Pedro"

def hora_mock(hour):
    return datetime(2025, 4, 7, hour, 0, 0)

def test_saludo_dias():
    hora = hora_mock(10)
    salida = ohce.run_ohce("Pedro", hora)
    assert salida == "¡Buenos días Pedro!"

def test_saludo_tardes():
    hora = hora_mock(15)
    salida = ohce.run_ohce("Pedro", hora)
    assert salida == "¡Buenas tardes Pedro!"

def test_saludo_noches():
    hora = hora_mock(21)
    salida = ohce.run_ohce("Pedro", hora)
    assert salida == "¡Buenas noches Pedro!"
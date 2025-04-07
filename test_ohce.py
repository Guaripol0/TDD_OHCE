from unittest.mock import patch
from datetime import datetime
import pytest
import ohce
def test_echo_reversed_word():
    assert ohce.echo("hello") == "hello"[::-1]
    assert ohce.echo("world") == "world"[::-1]
    assert ohce.echo("python") == "python"[::-1]

def test_echo_palindrome_word():
    assert ohce.echo("madam") == "madam\n¡Bonita palabra!"
    assert ohce.echo("racecar") == "racecar\n¡Bonita palabra!"
    assert ohce.echo("level") == "level\n¡Bonita palabra!"

def test_stop_returns_goodbye():
    assert ohce.echo("Stop!", name="Pedro") == "Adios Pedro"

def mock_datetime(hour):
    return datetime(2025, 4, 7, hour, 0, 0)

@patch("ohce.datetime")
def test_saludo_dias(mock_dt):
    mock_dt.now.return_value = mock_datetime(10)
    mock_dt.now.return_value.time = lambda: mock_datetime(10).time()
    salida = saludo("Pedro", "10:00")
    assert salida.startswith("¡Buenos días Pedro!")

@patch("ohce.datetime")
def test_saludo_tardes(mock_dt):
    mock_dt.now.return_value = mock_datetime(15)
    mock_dt.now.return_value.time = lambda: mock_datetime(15).time()
    salida = saludo("Pedro", "15:00")
    assert salida.startswith("¡Buenas tardes Pedro!")

@patch("ohce.datetime")
def test_saludo_noches(mock_dt):
    mock_dt.now.return_value = mock_datetime(21)
    mock_dt.now.return_value.time = lambda: mock_datetime(21).time()
    salida = saludo("Pedro", "21:00")
    assert salida.startswith("¡Buenas noches Pedro!")
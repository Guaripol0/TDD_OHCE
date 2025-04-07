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
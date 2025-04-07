import pytest
import ohce
def test_echo_reversed_word():
    assert ohce.echo("hello") == "hello"[::-1]

def test_echo_palindrome_word():
    assert ohce.echo("madam") == "madam\n ¡Bonita palabra!"

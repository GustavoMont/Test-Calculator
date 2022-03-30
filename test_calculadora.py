from Calculadora import Calculadora
import pytest

calculadora = Calculadora()

def test_soma():
    assert calculadora.Soma(5, 3) == 8

def test_subtracao():
    assert calculadora.Subtracao(5, 3) == 2

def test_multiplicacao():
    assert calculadora.Multiplicacao(5, 3) == 15

def test_divisao():
    assert calculadora.Divisao(5, 3) == 5/3
    with pytest.raises(ValueError):
        calculadora.Divisao(8, 0)

def test_fatorial():
    assert calculadora.Fatorial(5) == 120
    assert calculadora.Fatorial(0) == 1
    with pytest.raises(ValueError):
        calculadora.Fatorial(-8)

def test_potencia():
    assert calculadora.Potencia(5, 3) == 125
    assert calculadora.Potencia(5, 0) == 1
    with pytest.raises(ValueError):
        calculadora.Potencia(5, -3)
    
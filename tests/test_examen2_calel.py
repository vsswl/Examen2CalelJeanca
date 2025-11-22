import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Examen2 import MiClase

# Tests para ObtieneValencia(self, numero)

def test_Test1ObtieneValencia():
    assert MiClase(5, 120, 12, [], []).ObtieneValencia(102030405) == 3

def test_Test2ObtieneValencia():
    assert MiClase(5, 120, 12, [], []).ObtieneValencia(123123123) == 6

# Tests para DivisibleTempo(self, numero)

def test_Test1DivisibleTempo():
    assert MiClase(5, 120, 12, [], []).DivisibleTempo(25) == [1, 5, 25]

def test_Test2DivisibleTempo():
    assert MiClase(5, 120, 12, [], []).DivisibleTempo(18) == [1, 2, 3, 6, 9, 18]

# Tests para ObtieneMasBailable(self, lista)

def test_Test1ObtieneMasBailable():
    assert MiClase(5, 120, 12, [], []).ObtieneMasBailable([1.0, 0.0, 0.5]) == 1.0

def test_Test2ObtieneMasBailable():
    assert MiClase(5, 120, 12, [], []).ObtieneMasBailable([0.9, 0.9, 0.7, 0.8]) == 0.9

# Tests para VerificaListaCanciones(self, lista)

def test_Test1VerificaListaCanciones():
    assert MiClase(5, 120, 12, [], []).VerificaListaCanciones([None, None, "Butterflies"]) == False

def test_Test2VerificaListaCanciones():
    assert MiClase(5, 120, 12, [], []).VerificaListaCanciones(["The Way You Make Me Feel", "Ben", "Dirty Diana", "Don't Stop 'Til You Get Enough", "You Rock My World"]) == True

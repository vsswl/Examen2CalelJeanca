import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Examen2 import MiClase


## -- Test ObtieneValencia

def test_Test1ObtieneValencia():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.ObtieneValencia(13579) == 5

def test_Test2ObtieneValencia():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.ObtieneValencia(0) == 0



## -- Test DivisibleTempo

def test_Test1DivisibleTempo():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.DivisibleTempo(0) == []

def test_Test2DivisibleTempo():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.DivisibleTempo(11) == [1, 11]



# -- Test ObtieneMasBailable

def test_Test1ObtieneMasBailable():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.ObtieneMasBailable([1, 0.1, 0.2, 0.9, 0.5]) == 1

def test_Test2ObtieneMasBailable():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.ObtieneMasBailable([]) == None



## -- Test VerificaListaCanciones

def test_Test1VerificaListaCanciones():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.VerificaListaCanciones(['Metallica', 'Queen', None]) == False

def test_Test2VerificaListaCanciones():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.VerificaListaCanciones([]) == True


## -- Test Encuentra

def test_Test1Encuentra():
    obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    assert obj.Encuentra([], 0) == False


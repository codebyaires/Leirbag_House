import pytest
from src.multiplicarf import multiplicar

def test_multiplicar():
    if multiplicar(0,1) != 0:
        assert False
    if multiplicar(1,0) != 0:
        assert False
    if multiplicar(2,3) != 6:
        assert False
    if multiplicar(5,4) != 20:
        assert False
    if multiplicar(10,2) != 20:
        assert False
    if multiplicar(-1, 3) != -3:
        assert False
    if multiplicar(3, -2) != -6:
        assert False
    if multiplicar(1, 1) == 1:
        assert True
    print ("Todos os testes passaram com sucesso!")
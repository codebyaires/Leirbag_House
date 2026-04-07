import pytest
from subtrairf import subtrair

def test_subtrair():
    if subtrair(5, 3) != 2:
        assert False
    if subtrair(10, 4) != 6:
        assert False
    if subtrair(0, 0) != 0:
        assert False
    if subtrair(-5, -3) != -2:
        assert False
    if subtrair(-10, 4) != -14:
        assert False
    if subtrair(5, -3) != 8:
        assert False
    if subtrair(3.5, 1.2) != 2.3:
        assert False
    if subtrair(-2.5, -1.5) != -1.0:
        assert False
    if subtrair(1 ,1) == 0:
        assert True
    print ("Todos os testes passaram com sucesso!")
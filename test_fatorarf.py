import pytest
from fatorarf import fatorar

def test_fatorar():
    if fatorar(0,1) != 0:
        assert False
    if fatorar(1,0) != 1:
        assert False
    if fatorar(2,3) != 8:
        assert False
    if fatorar(5,4) != 625:
        assert False
    if fatorar(10,2) != 100:
        assert False
    if fatorar(-1, 3) != -1:
        assert False
    if fatorar(3, -2) != 1:
        assert False
    if fatorar(1, 1) == 1:
        assert True
    print ("Todos os testes passaram com sucesso!")
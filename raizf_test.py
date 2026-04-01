import pytest
import raizf

def test_raiz():
    if raizf.raiz(9)!= 3:
        assert False
    if raizf.raiz(25)!= 5:
        assert False
    if raizf.raiz(2)!= pytest.approx(2**0.5):
        assert False
    assert True
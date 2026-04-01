import pytest
import dividirf

def test_dividir():
    if dividirf.dividir(10, 2)["resultado"] != 5:
        assert False
    if dividirf.dividir(-10, 2)["resultado"] != -5:
        assert False
    if dividirf.dividir(10, 3)["resultado"] != pytest.approx(10/3):
        assert False
    try:
        dividirf.dividir(5, 0)
        assert False
    except ZeroDivisionError:
        pass
    assert True
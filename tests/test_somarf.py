import pytest
import src.somarf as somarf

def test_somar():
    if somarf.somar(0, 0)["resultado"] != 0:
        assert False
    if somarf.somar(-1, -1)["resultado"] != -2:
        assert False
    if somarf.somar(2, 2)["resultado"] != 4:
        assert False
    if somarf.somar(2, -2)["resultado"] != 0:
        assert False
    if somarf.somar(0.2, 0.3)["resultado"]  != pytest.approx(0.5):
        assert False
    try:
        somarf.somar()
        assert False
    except TypeError:
        pass
    assert True

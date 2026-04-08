from src.exponenciarf import exponenciar

def test_exponenciar():
    if exponenciar(2, 3) != 8:
        assert False
    if exponenciar(5, 4) != 625:
        assert False
    if exponenciar(10, 2) != 100:
        assert False
    if exponenciar(-1, 3) != -1:
        assert False
    if exponenciar(3, -2) != 1/9:
        assert False
    if exponenciar(-2, -3) != -0.125:
        assert False
    if exponenciar(1, 0) != 1:
        assert False
    if exponenciar(0, 1) != 0:
        assert False
    if exponenciar(1, 2) == 1:
        assert True
    print("Todos os testes passaram com sucesso!")


   
def soma(a, b):
    return a+b


def subtrai(a, b):
    return a-b

# testes


def test_soma():
    assert soma(5, 4) == 9


def test_sub():
    assert subtrai(10, 3) == 7

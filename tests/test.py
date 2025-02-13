import pytest

from source import Calculadora

@pytest.mark.parametrize("test_input_a,test_input_b,expected", [(5,3,8),pytest.param(10,15,18,marks=pytest.mark.xfail)])
def test_soma(test_input_a,test_input_b,expected):
    assert Calculadora.soma(test_input_a,test_input_b) == expected

@pytest.mark.parametrize("test_input_a,test_input_b,expected", [(51,50,1),pytest.param(20,35,23,marks=pytest.mark.xfail)])
def test_subtracao(test_input_a,test_input_b,expected):
    assert Calculadora.subtracao(test_input_a,test_input_b) == expected

@pytest.mark.parametrize("test_input_a,test_input_b,expected", [(6,5,30),pytest.param(1,6,18,marks=pytest.mark.xfail)])
def test_multiplicacao(test_input_a,test_input_b,expected):
    assert Calculadora.multiplicacao(test_input_a,test_input_b) == expected

@pytest.mark.parametrize("test_input_a,test_input_b,expected", [(55,11,5),pytest.param(100,20,6,marks=pytest.mark.xfail)])
def test_divisao(test_input_a,test_input_b,expected):
    assert Calculadora.divisao(test_input_a,test_input_b) == expected

def test_divisao_zero():
    with pytest.raises(ZeroDivisionError) as extxt:
        Calculadora.divisao(1, 0)
    assert str(extxt.value) == "Divisão por zero não permitida."
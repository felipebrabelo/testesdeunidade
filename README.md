# Testes de unidade

## Aplicação

A aplicação se trata de uma calculadora que realiza as 4 operações básicas: soma, subtração, multiplicação e divisão, com a divisão possuindo um tratamento de exceção em caso de divisão por 0.

## Testes

Para cada método foi criado um teste (test_soma, test_subtacao, test_mutiplicacao, test_divisao) que verifica se o método retorna corretamente o resultado da operação, sendo parametrizados por test_input_a e test_input_b para as entradas e expected para a saida, sendo passados valores corretos, por exemplo, (5,3,8) para a soma (5+3=8) e valores incorretos, por exemplo (10,15,18) para a soma (10+15!=18), para explorar melhor o funcionamento dos testes em pytest. Por fim, um método extra para a operação de divisão (test_divisao_zero) para testar se o tratamento da exceção de divisão por zero está sendo feito corretamente.

## Como aplicar o teste

Caso não tenha instalado, instalar o pytest (requer Python 3.8+):

`pip install -U pytest`

Após clonar o diretório, dentro dele usar o seguinte comando no terminal:

`pytest -v tests/test.py`

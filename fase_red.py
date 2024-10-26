#fase_red
#Testes para a função calcular_media (ainda não implementada)

import unittest

def test_calculo_media():
    assert calcular_media(7.0, 8.0, 9.0) == 8.0

def test_todas_as_notas_zero():
    assert calcular_media(0, 0, 0) == 0.0

def test_todas_as_notas_maximas():
    assert calcular_media(10.0, 10.0, 10.0) == 10.0

def test_valores_decimais():
#Verificar se a média de valores decimais funciona corretamente
    assert calcular_media(5.5, 6.5, 7.5) == 6.5

def test_notas_invalidas():
#Teste para garantir que uma exceção é levantada para valores fora do intervalo
    try:
        calcular_media(11, 5, 7)
    except ValueError as e:
        assert str(e) == "As notas devem estar entre 0 e 10."

def test_entrada_nao_numerica():
#Teste para verificar se o código lida com entradas não numéricas
    try:
        calcular_media("dez", 5, 7)
    except TypeError as e:
        assert str(e) == "As notas devem ser números."

if __name__ == "__main__":
    unittest.main()
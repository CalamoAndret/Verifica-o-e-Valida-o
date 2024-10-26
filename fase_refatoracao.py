#fase_refatoracao

import unittest

def calcular_media(nota1, nota2, nota3):
    notas = [nota1, nota2, nota3]
    
    #Verifica se todas as entradas são números
    if not all(isinstance(nota, (int, float)) for nota in notas):
        raise TypeError("As notas devem ser números.")
    
    #Verifica se as notas estão no intervalo permitido (0 a 10)
    if not all(0 <= nota <= 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10.")
    
    #Cálculo da média
    return round((nota1 + nota2 + nota3) / 3, 2)  # Arredonda a média para 2 casas decimais

#Classe de testes
class TestCalcularMedia(unittest.TestCase):
    def test_calculo_media(self):
        self.assertEqual(calcular_media(7.0, 8.0, 9.0), 8.0)

    def test_todas_as_notas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0.0)

    def test_todas_as_notas_maximas(self):
        self.assertEqual(calcular_media(10.0, 10.0, 10.0), 10.0)

    def test_valores_decimais(self):
        self.assertEqual(calcular_media(5.5, 6.5, 7.5), 6.5)

    def test_notas_invalidas(self):
        with self.assertRaises(ValueError) as context:
            calcular_media(11, 5, 7)  #Nota fora do intervalo
        self.assertEqual(str(context.exception), "As notas devem estar entre 0 e 10.")

    def test_entrada_nao_numerica(self):
        with self.assertRaises(TypeError) as context:
            calcular_media("dez", 5, 7)  #Entrada não numérica
        self.assertEqual(str(context.exception), "As notas devem ser números.")

if __name__ == "__main__":
    unittest.main()

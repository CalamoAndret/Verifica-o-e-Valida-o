#fase_green

import unittest

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3  

# Classe de testes
class TestCalcularMedia(unittest.TestCase):
    def test_calculo_media(self):
        self.assertEqual(calcular_media(7.0, 8.0, 9.0), 8.0)

    def test_todas_as_notas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0.0)

    def test_todas_as_notas_maximas(self):
        self.assertEqual(calcular_media(10.0, 10.0, 10.0), 10.0)

    def test_valores_decimais(self):
        self.assertEqual(calcular_media(5.5, 6.5, 7.5), 6.5)


if __name__ == "__main__":
    unittest.main()

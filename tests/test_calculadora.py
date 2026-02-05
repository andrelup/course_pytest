from mi_proyecto.main import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5
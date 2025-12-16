from main import entero_a_romano

def test_entero_a_romano():
    assert entero_a_romano(1994) == "MCMXCIV"

def test_entero_a_romano():
    assert entero_a_romano(3) == "III"

def test_entero_a_romano():
    assert entero_a_romano(33) == "XXXIII"

def test_entero_a_romano():
    assert entero_a_romano(333) == "CCCXXXIII"
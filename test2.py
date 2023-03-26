from bank1 import value


def test_h():
    assert value("h") == 20
    assert value("hey") == 20

def test_hello():
    assert value("hello") == 0
    assert value("hey") != 0

def test_else():    
    assert value("bonjour") == 100
    assert value ("joni") == 100


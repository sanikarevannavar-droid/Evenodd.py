from even_odd import check_even_odd

def test_even_number():
    assert check_even_odd(6) == "Even"

def test_odd_number():
    assert check_even_odd(7) == "Odd"

def test_zero():
    assert check_even_odd(0) == "Even"

def test_negative_number():
    assert check_even_odd(-4) == "Even"
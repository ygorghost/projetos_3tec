from app.app import create_app
from fizzbuzz import fizzbuzz

flask_app = create_app()

def test_fizz():
    res = fizzbuzz(3)
    assert res == 'fizz' 

def test_fizz():
    res = fizzbuzz(5)
    assert res == 'buzz' 

def test_fizz():
    res = fizzbuzz(15)
    assert res == 'fizzbuzz' 

def test_fizz():
    res = fizzbuzz(1)
    assert res == 'fizzbuzz' 
    
import os
import string
import types
import pytest
def test_function_file_exist():
    """Tested  if file exists """
    assert os.path.exists('main.py') == True


def test_function_exist():
    ''' Test if the function in main.py file '''
    from main import string_calculator
    assert isinstance(string_calculator,types.FunctionType)

from main import string_calculator
    
def test_function_args_is_none_raise_typeerror():
    ''' Test if an argument passed is None and it raises TypeError'''
    with pytest.raises(TypeError):
        string_calculator(None)
    
def test_function_args_is_not_string_raises_typeerror():
    ''' Test if an argument passed is not a string raises TypeError'''
    with pytest.raises(TypeError):
        string_calculator(0)

def test_function__arg_is_empty_return_zero():
    '''Test if an empty string is passed  returns 0'''
    output = string_calculator("")
    assert output == 0
    

def test_function_args_is_passed_with_one_number():
    '''Test if an string with 1 is passed return 1'''
    output = string_calculator('1')
    assert output == 1
    
def test_function_args_is_passed_with_two_number_with_space():
    '''Test if an string is passed return correct'''
    output = string_calculator('1 2')
    assert output == 3

def test_function_args_is_passed_with_two_number_with_space():
    '''Test if an string with space is passed return correct'''
    output = string_calculator('1 2')
    assert output == 3
def test_function_args_is_passed_with_two_number_with_newline():
    '''Test if an string with newline is passed return correct'''
    output = string_calculator('1\n2')
    assert output == 3  

def test_function_args_is_passed_with_two_number_with_comma_with_newline_at_end():
    '''Test if an string with  '''
    with pytest.raises(SyntaxError):
        output = string_calculator('1,2,\n')

def test_function_args_is_passed_with_two_number_with_comma():
    '''Test if an string with comma is passed return correct'''
    output = string_calculator('1,2')
    assert output == 3

def test_function_args_is_passed_with_two_number_with_comma_more():
    '''Test id an string with more number is passed return the correct sum'''
    output = string_calculator('1000,2000,100,200')
    assert output == 3300


def test_function_args_is_passed_with_delimiter_change_syntax():
    '''Test the option of delimiter change using // '''
    output = string_calculator('//;\n1000;2000;100;200')
    assert output == 3300
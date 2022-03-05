import os
import string
import types
import pytest
def test_function_file_exist():
    """Tested  if file exists """
    assert os.path.exists('main.py') == True


def test_function_exist():
    ''' Test if the function in main.py file '''
    from main import Add
    assert isinstance(Add,types.FunctionType)

from main import Add
    
def test_function_args_is_none_raise_typeerror():
    ''' Test if an argument passed is None and it raises TypeError'''
    with pytest.raises(TypeError):
        Add(None)
    
def test_function_args_is_not_string_raises_typeerror():
    ''' Test if an argument passed is not a string raises TypeError'''
    with pytest.raises(TypeError):
        Add(0)

def test_function__arg_is_empty_return_zero():
    '''Test if an empty string is passed  returns 0'''
    output = Add("")
    assert output == 0
    

def test_function_args_is_passed_with_one_number():
    '''Test if an string with 1 is passed return 1'''
    output = Add('1')
    assert output == 1
    
def test_function_args_is_passed_with_two_number_with_space():
    '''Test if an string is passed return correct'''
    output = Add('1 2')
    assert output == 3

def test_function_args_is_passed_with_two_number_with_space():
    '''Test if an string with space is passed return correct'''
    output = Add('1 2')
    assert output == 3
def test_function_args_is_passed_with_two_number_with_newline():
    '''Test if an string with newline is passed return correct'''
    output = Add('1\n2')
    assert output == 3  

def test_function_args_is_passed_with_two_number_with_comma_with_newline_at_end():
    '''Test if an string with  '''
    with pytest.raises(SyntaxError):
        output = Add('1,2,\n')

def test_function_args_is_passed_with_two_number_with_comma():
    '''Test if an string with comma is passed return correct'''
    output = Add('1,2')
    assert output == 3

def test_function_args_is_passed_with_two_number_with_comma_more():
    '''Test id an string with more number is passed return the correct sum'''
    output = Add('1000,2000,100,200')
    assert output == 3300


def test_function_args_is_passed_with_delimiter_change_syntax():
    '''Test the option of delimiter change using // '''
    output = Add('//;\n1000;2000;100;200')
    assert output == 3300
    
def test_function_args_is_passed_with_delimiter_change_syntax_with_negatives():
    '''Test the option of delimiter change using // with negatives and ValueError '''
    with pytest.raises(ValueError):
        output = Add('//;\n1000;2000;100;-200')
    
    
def test_function_args_is_passed_with_delimiter_change_syntax_with_negatives_all():
    '''Test the option of delimiter change using // '''
    with pytest.raises(ValueError):
        output = Add('//;\n1000;2000;100;-200;-400')
    
    
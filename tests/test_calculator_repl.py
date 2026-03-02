import datetime
from pathlib import Path
import pandas as pd
import pytest
from unittest.mock import Mock, patch, PropertyMock
from decimal import Decimal
from tempfile import TemporaryDirectory
from app.calculator_repl import calculator_repl
from app.operations import Operations


@patch('builtins.input', side_effect=['add', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_addition(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 5")

@patch('builtins.input', side_effect=['subtract', '5', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_subtraction(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 2")

@patch('builtins.input', side_effect=['multiply', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_multiply(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 6")

@patch('builtins.input', side_effect=['divide', '6', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_division(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 2")

@patch('builtins.input', side_effect=['power', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_power(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 8")

@patch('builtins.input', side_effect=['power', 'cancel', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_power_cancelled(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Operation cancelled")


@patch('builtins.input', side_effect=['root', '16', '2', 'exit'])
@patch('builtins.print')
def test_calculator_repl_root(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 4.000000000000000000000000000")

@patch('builtins.input', side_effect=['root', '16', 'cancel', 'exit'])
@patch('builtins.print')
def test_calculator_repl_root_cancelled(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Operation cancelled")

@patch('builtins.input', side_effect=['int_divide', '7', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_integer_division(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 2")

@patch('builtins.input', side_effect=['modulus', '7', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_modulus(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 1")

@patch('builtins.input', side_effect=['abs_diff', '3', '6', 'exit'])
@patch('builtins.print')
def test_calculator_repl_absolute_difference(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 3")

@patch('builtins.input', side_effect=['percent', '3', '10', 'exit'])
@patch('builtins.print')
def test_calculator_repl_percentage(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("\nResult: 30.0")


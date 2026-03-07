import datetime
from pathlib import Path
import pandas as pd
import pytest
from unittest.mock import Mock, patch, PropertyMock
from decimal import Decimal
from tempfile import TemporaryDirectory
from app.calculator_repl import calculator_repl
from app.operations import Operation, OperationFactory

@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_exit(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Goodbye!")

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
    mock_print.assert_any_call("\nResult: 4")

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


@patch('builtins.input', side_effect=['divide', '6', '0'])
@patch('builtins.print')
def calculator_repl_division(mock_print, mock_input):
    with pytest.raises(ZeroDivisionError) as exc_info:
           calculator_repl()
    assert str(exc_info.value) == "Cannot divide by zero. Please enter a non-zero divisor."

@patch('builtins.input', side_effect=['history','exit'])
@patch('builtins.print')
def test_calculator_repl_no_history(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("No calculations performed yet")

@patch('builtins.input', side_effect=['modulus', '7', '3','history','exit'])
@patch('builtins.print')
def test_calculator_repl_some_history(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Calculation history: ")
    mock_print.assert_any_call("1. Modulus: 7 modulus 3 = 1")
    mock_print.assert_any_call("Goodbye!")

@patch('builtins.input', side_effect=['help','exit'])
@patch('builtins.print')
def test_calculator_repl_help_exit(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Calculator started. Type 'help' for commands./")
    mock_print.assert_any_call("Goodbye!")

import datetime
from pathlib import Path
import pandas as pd
import pytest
from unittest.mock import Mock, patch, PropertyMock
from decimal import Decimal
from tempfile import TemporaryDirectory
from app.calculator_repl import calculator_repl
from app.operations import Operation, OperationFactory
from app.exceptions import ValidationError, OperationError
from colorama import Fore, Back, Style

@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_exit(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Back.BLUE + "Goodbye!" + Style.RESET_ALL)

@patch('builtins.input', side_effect=['add', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_addition(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 5")

@patch('builtins.input', side_effect=['subtract', '5', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_subtraction(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 2")

@patch('builtins.input', side_effect=['multiply', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_multiply(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 6")

@patch('builtins.input', side_effect=['divide', '6', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_division(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 2")

@patch('builtins.input', side_effect=['power', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_power(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 8")

@patch('builtins.input', side_effect=['power', 'cancel', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_power_cancelled(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Back.YELLOW + "Operation cancelled" + Style.RESET_ALL)


@patch('builtins.input', side_effect=['root', '16', '2', 'exit'])
@patch('builtins.print')
def test_calculator_repl_root(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 4")

@patch('builtins.input', side_effect=['root', '16', 'cancel', 'exit'])
@patch('builtins.print')
def test_calculator_repl_root_cancelled(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Back.YELLOW + "Operation cancelled" + Style.RESET_ALL)

@patch('builtins.input', side_effect=['int_divide', '7', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_integer_division(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 2")

@patch('builtins.input', side_effect=['modulus', '7', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_modulus(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 1")

@patch('builtins.input', side_effect=['abs_diff', '3', '6', 'exit'])
@patch('builtins.print')
def test_calculator_repl_absolute_difference(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 3")

@patch('builtins.input', side_effect=['percent', '3', '10', 'exit'])
@patch('builtins.print')
def test_calculator_repl_percentage(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nResult: 30.0")


@patch('builtins.input', side_effect=['clear','history','exit'])
@patch('builtins.print')
def test_calculator_repl_no_history(mock_print, mock_input):
    calculator_repl()

    mock_print.assert_any_call(Fore.LIGHTYELLOW_EX + "No calculations in history")

@patch('builtins.input', side_effect=['clear','modulus', '7', '3','history','exit'])
@patch('builtins.print')
def test_calculator_repl_some_history(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.GREEN + "\nCalculation History:")
    mock_print.assert_any_call(Fore.GREEN + "1. Modulus(7, 3) = 1")

@patch('builtins.input', side_effect=['help','exit'])
@patch('builtins.print')
def test_calculator_repl_help_exit(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Back.BLUE + "Calculator started. Type 'help' for commands." + Style.RESET_ALL)
    mock_print.assert_any_call(Back.MAGENTA +"\nAvailable commands:")
    mock_print.assert_any_call(Back.MAGENTA +"  add, subtract, multiply, divide, power, root - Perform calculations")
    mock_print.assert_any_call(Back.MAGENTA +"  modulus, int_divide, percent, abs_diff - Perform calculations")
    mock_print.assert_any_call(Back.MAGENTA +"  history - Show calculation history")
    mock_print.assert_any_call(Back.MAGENTA +"  clear - Clear calculation history")
    mock_print.assert_any_call(Back.MAGENTA +"  undo - Undo the last calculation")
    mock_print.assert_any_call(Back.MAGENTA +"  redo - Redo the last undone calculation")
    mock_print.assert_any_call(Back.MAGENTA +"  save - Save calculation history to file")
    mock_print.assert_any_call(Back.MAGENTA + "  load - Load calculation history from file")
    mock_print.assert_any_call(Back.MAGENTA + "  exit - Exit the calculator" + Style.RESET_ALL)

# Test REPL Commands (using patches for input/output handling)

@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_save_hist_exit(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history') as mock_save_history:
        calculator_repl()
        mock_save_history.assert_called_once()
        mock_print.assert_any_call(Fore.GREEN + "History saved successfully.")
        mock_print.assert_any_call(Back.BLUE + "Goodbye!" + Style.RESET_ALL)

@patch('builtins.input', side_effect=['save','exit'])
@patch('builtins.print')
def test_calculator_repl_save_history(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history') as mock_save_history:
        calculator_repl()
        mock_print.assert_any_call(Fore.GREEN + "History saved successfully.")
        mock_print.assert_any_call(Back.BLUE + "Goodbye!" + Style.RESET_ALL)

@patch('builtins.input', side_effect=['load','exit'])
@patch('builtins.print')
def test_calculator_repl_load_history(mock_print, mock_input):
    with patch('app.calculator.Calculator.load_history') as mock_load_history:
        calculator_repl()
        mock_print.assert_any_call(Fore.GREEN + "History loaded successfully")
        mock_print.assert_any_call(Back.BLUE + "Goodbye!" + Style.RESET_ALL)

@patch('builtins.input', side_effect=['undo','exit'])
@patch('builtins.print')
def test_calculator_repl_undo(mock_print, mock_input):
    with patch('app.calculator.Calculator.undo') as mock_undo:
        calculator_repl()
        mock_print.assert_any_call(Fore.GREEN + "Operation undo done")
        mock_print.assert_any_call(Back.BLUE + "Goodbye!" + Style.RESET_ALL)

@patch('builtins.input', side_effect=['redo','exit'])
@patch('builtins.print')
def test_calculator_repl_redo(mock_print, mock_input):
    with patch('app.calculator.Calculator.redo') as mock_redo:
        calculator_repl()
        mock_print.assert_any_call(Fore.GREEN + "Operation redo done")
        mock_print.assert_any_call(Back.BLUE + "Goodbye!" + Style.RESET_ALL)

@patch('builtins.input', side_effect=['undo','exit'])
@patch('builtins.print')
def test_calculator_repl_undo(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.LIGHTYELLOW_EX + "Nothing to undo")
    mock_print.assert_any_call(Back.BLUE + "Goodbye!" + Style.RESET_ALL)

@patch('builtins.input', side_effect=['redo','exit'])
@patch('builtins.print')
def test_calculator_repl_redo(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(Fore.LIGHTYELLOW_EX + "Nothing to redo")
    mock_print.assert_any_call(Back.BLUE + "Goodbye!" + Style.RESET_ALL)

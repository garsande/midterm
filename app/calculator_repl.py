########################
# Calculator REPL #
########################
from decimal import Decimal
import logging

from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError
from app.history import AutoSaveObserver, LoggingObserver
from app.operations import OperationFactory
from colorama import init, Fore, Back, Style

def calculator_repl():
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """
    try:
        calc = Calculator()

        # Register observers for logging and auto-saving history
        calc.add_observer(LoggingObserver())
        calc.add_observer(AutoSaveObserver(calc))
        print(Back.BLUE + "Calculator started. Type 'help' for commands." + Style.RESET_ALL)
        while True:
            try:
               
                command = input(Fore.BLUE + "\nEnter command: ").lower().strip()  # Prompt the user for a command

                if command == 'help':
                    # Display available commands
                    print(Back.MAGENTA + "\nAvailable commands:")
                    print(Back.MAGENTA + "  add, subtract, multiply, divide, power, root - Perform calculations")
                    print(Back.MAGENTA + "  modulus, int_divide, percent, abs_diff, log - Perform calculations")
                    print(Back.MAGENTA + "  history - Show calculation history")
                    print(Back.MAGENTA + "  clear - Clear calculation history")
                    print(Back.MAGENTA + "  undo - Undo the last calculation")
                    print(Back.MAGENTA + "  redo - Redo the last undone calculation")
                    print(Back.MAGENTA + "  save - Save calculation history to file")
                    print(Back.MAGENTA + "  load - Load calculation history from file")
                    print(Back.MAGENTA + "  exit - Exit the calculator" + Style.RESET_ALL)
                    continue

                if command == 'exit':
                    # Attempt to save history before exiting
                    try:
                        calc.save_history()
                        print(Fore.GREEN + "History saved successfully.")
                    except Exception as e:
                        print(Fore.RED + f"Warning: Could not save history: {e}")
                    print(Back.BLUE + "Goodbye!" + Style.RESET_ALL)
                    break

                if command == 'history':
                    # Display calculation history
                    history = calc.show_history()
                    if not history:
                        print(Fore.LIGHTYELLOW_EX + "No calculations in history")
                    else:
                        print(Fore.GREEN + "\nCalculation History:")
                        for i, entry in enumerate(history, 1):
                            print(Fore.GREEN + f"{i}. {entry}")
                    continue

                if command == 'clear':
                    # Clear calculation history
                    calc.clear_history()
                    print(Fore.GREEN + "History cleared")
                    continue

                if command == 'save':
                    # Save calculation history to file
                    try:
                        calc.save_history()
                        print(Fore.GREEN + "History saved successfully")
                    except Exception as e:
                        print(Fore.RED + f"Error saving history: {e}")
                    continue

                if command == 'load':
                    # Load calculation history from file
                    try:
                        calc.load_history()
                        print(Fore.GREEN + "History loaded successfully")
                    except Exception as e:
                        print(Fore.RED + f"Error loading history: {e}")
                    continue
                    
                if command == 'undo':
                    # Undo the last calculation
                    if calc.undo():
                        print(Fore.GREEN + "Operation undo done")
                    else:
                        print(Fore.LIGHTYELLOW_EX + "Nothing to undo")
                    continue

                if command == 'redo':
                    # Redo the last undone calculation
                    if calc.redo():
                        print(Fore.GREEN + "Operation redo done")
                    else:
                        print(Fore.LIGHTYELLOW_EX + "Nothing to redo")
                    continue

                if command in ['add', 'subtract', 'multiply', 'divide', 'power', 'root',
                               'modulus', 'int_divide', 'percent', 'abs_diff', 'log']:
                    # Perform the specified arithmetic operation
                    try:
                        print(Style.BRIGHT + "\nEnter numbers (or 'cancel' to abort):")
                        a = input(Fore.BLUE + "First number: ")
                        if a.lower() == 'cancel':
                            print(Back.YELLOW + "Operation cancelled" + Style.RESET_ALL)
                            continue
                        b = input(Fore.BLUE + "Second number: ")
                        if b.lower() == 'cancel':
                            print(Back.YELLOW + "Operation cancelled" + Style.RESET_ALL)
                            continue

                        # Create the appropriate operation instance using the Factory pattern
                        operation = OperationFactory.create_operation(command)
                        calc.set_operation(operation)

                        # Perform the calculation
                        result = calc.perform_operation(a, b)

                        # Normalize the result if it's a Decimal
                        if isinstance(result, Decimal):
                            result = result.normalize()

                        print(Fore.GREEN + f"\nResult: {result}")
                    except (ValidationError, OperationError) as e:
                        # Handle known exceptions related to validation or operation errors
                        print(Fore.RED + f"Error: {e}")
                    except Exception as e:
                        # Handle any unexpected exceptions
                        print(Fore.RED + f"Unexpected error: {e}")
                    continue

                # Handle unknown commands
                print(Fore.RED + f"Unknown command: '{command}'. Type 'help' for available commands.")

            except KeyboardInterrupt:
                # Handle Ctrl+C interruption gracefully
                print(Fore.RED + "\nOperation cancelled")
                continue
            except EOFError:
                # Handle end-of-file (e.g., Ctrl+D) gracefully
                print(Fore.RED + "\nInput terminated. Exiting...")
                break
            except Exception as e:
                # Handle any other unexpected exceptions
                print(Fore.RED + f"Error: {e}")
                continue

    except Exception as e:
        # Handle fatal errors during initialization
        print(Fore.RED + f"Fatal error: {e}")
        logging.error(f"Fatal error in calculator REPL: {e}")
        raise

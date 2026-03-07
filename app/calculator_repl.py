########################
# Calculator REPL #
########################
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union
import logging

from app.operations import Operation, OperationFactory
from app.exceptions import ValidationError,OperationError

from app.calculator import Calculator

def calculator_repl():
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """
    calc = Calculator()
    history: List[Operation] = []

    try:

        print("Calculator started. Type 'help' for commands./")
        while True:
            try:
               
                command = input("\nEnter command: ").lower().strip()  # Prompt the user for a command

                if command == 'help':
                    # Display available commands
                    print("\nAvailable commands:")
                    print("  add, subtract, multiply, divide, power, root - Perform calculations")
                    print("  modulus, int_divide, percent, abs_diff - Perform calculations")
                    print("  history - Show calculation history")
                    # print("  clear - Clear calculation history")
                    # print("  save - Save calculation history to file")
                    # print("  load - Load calculation history from file")
                    print("  exit - Exit the calculator")
                    continue

                if command == 'exit':
                    print("Goodbye!")
                    break
                
                if command == 'history':
                    if not(history):
                        print("No calculations performed yet")
                    else:
                        print("Calculation history: ")
                        for idx, calculation in enumerate(history, start =1):
                             print(f"{idx}. {calculation}")
                    continue

                if command in ['add', 'subtract', 'multiply', 'divide', 'power', 'root',
                               'modulus', 'int_divide', 'percent', 'abs_diff']:
                    # Perform the specified arithmetic operation
                    try:
                        print("\nEnter numbers (or 'cancel' to abort):")
                        a = input("First number: ")
                        if a.lower() == 'cancel':
                            print("Operation cancelled")
                            continue
                        b = input("Second number: ")
                        if b.lower() == 'cancel':
                            print("Operation cancelled")
                            continue

                        # Create the appropriate operation instance using the Factory pattern
                        operation = OperationFactory.create_operation(command)
                        calc.set_operation(operation)

                        #Perform the calc
                        result = calc.perform_operation(a,b)
                        
                        # Normalize the result if it's a Decimal
                        if isinstance(result, Decimal):
                            result = result.normalize()

                        print(f"\nResult: {result}")
                        history.append(operation.getHistoryValue(a, b, command, result))

                    except (ValidationError, OperationError) as e:
                        # Handle known exceptions related to validation or operation errors
                        print(f"Error: {e}")
                    except Exception as e:
                        # Handle any unexpected exceptions
                        print(f"Unexpected error: {e}")
                    continue
                        
                # Handle unknown commands
                print(f"Unknown command: '{command}'. Type 'help' for available commands.")

            except KeyboardInterrupt:
                # Handle Ctrl+C interruption gracefully
                print("\nOperation cancelled")
                continue
            except EOFError:
                # Handle end-of-file (e.g., Ctrl+D) gracefully
                print("\nInput terminated. Exiting...")
                break
            except Exception as e:
                # Handle any other unexpected exceptions
                print(f"Error: {e}")
                continue

    except Exception as e:
        # Handle fatal errors during initialization
        print(f"Fatal error: {e}")
        logging.error(f"Fatal error in calculator REPL: {e}")
        raise

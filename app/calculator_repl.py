########################
# Calculator REPL #
########################
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union
import logging

from app.operations import Operations
from app.calculation import Calculation 
from app.calculation import CalculationFactory

def calculator_repl():
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """

    history: List[Calculation] = []

    try:

        print("Calculator started. Type 'help' for commands./")
        while True:
            try:
               
                command = input("\nEnter command: ").lower().strip()  # Prompt the user for a command

                if command == 'help':
                    # Display available commands
                    help_message = """
    Calculator REPL Help
    --------------------
    Available commands:
    add, subtract, multiply, divide, power, root, abs_diff, int_divide,
    modulus, percentage

    Special Commands:
        help      : Display this help message.
        history   : Show the history of calculations.
        exit      : Exit the calculator.

                            """
                    print(help_message)
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

                        #Handle conversion to Decimal from String
                        a = Decimal(str(a))
                        b = Decimal(str(b))
                    except (ValueError) as e:
                        # Handle known exceptions related to validation or operation errors
                        print(f"Error: {e}")
                        continue
                    except Exception as e:
                        # Handle any unexpected exceptions
                        print(f"Unexpected error: {e}")
                        continue
                    try:
                        # Create the appropriate operation instance using the Factory pattern
                            calculation =CalculationFactory().create_calculation(command,a,b)
                    except(ValueError) as e:
                            print(f"Error: {e}")
                            continue
                    try:
                            result = calculation.execute()
                    except ZeroDivisionError:
                            # Handle division by zero specifically
                            print("Cannot divide by zero. Please enter a non-zero divisor.")
                            continue  # Prompt the user again
                    except Exception as e:
                            # Handle any other unforeseen exceptions
                            print(f"An error occurred during calculation: {e}. Please try again.")
                            continue  # Prompt the user again
                        
                    print(f"\nResult: {result}")
                    history.append(calculation)
                else:       
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
        #logging.error(f"Fatal error in calculator REPL: {e}")
        raise

########################
# Calculator REPL #
########################
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union
import logging

from app.operations import Operations


def calculator_repl():
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """
    try:

        print("Calculator started. Type 'help' for commands./")
        while True:
            try:
               
                command = input("\nEnter command: ").lower().strip()  # Prompt the user for a command

                if command == 'help':
                    # Display available commands
                    print("\nAvailable commands:")
                    print("  add, subtract, multiply, divide, power, root,abs_ - Perform calculations")
                    print("  exit - Exit the calculator")
                    continue

                if command == 'exit':
                    print("Goodbye!")
                    break

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


                        a = Decimal(str(a))
                        b = Decimal(str(b))

                        # Create the appropriate operation instance using the Factory pattern
                        if command.lower() == "add":
                            result = Operations.addition(a, b)  # We call the addition function to add the two numbers.
                        elif command.lower() == "subtract":
                            result = Operations.subtraction(a, b)  # We call the subtraction function to subtract the two numbers.
                        elif command.lower() == "multiply":
                            result = Operations.multiplication(a, b)  # We call the multiplication function to multiply the two numbers.
                        elif command.lower() == "divide":
                            try:
                                result = Operations.division(a, b)  # We call the division function to divide the two numbers.
                            except ValueError as e:
                                # This part handles the case where someone tries to divide by zero, which we can't do.
                                # The division function will throw an error if someone tries dividing by zero, and we catch that error here.
                                print(e)  # Show the error message.
                                continue  # Go back to the top of the loop and try again.
                        elif command.lower() == "power":
                            try:
                                result = Operations.power(a, b)  # We call the power function to find the power of the base to exponent
                            except ValueError as e:
                                # This part handles the case where someone tries to raise power by a  negative number, which we can't do.
                                # The power function will throw an error if someone tries raising power by a negative number, and we catch that error here.
                                print(e)  # Show the error message.
                                continue  # Go back to the top of the loop and try again.
                        elif command.lower() == "root":
                            try:
                                result = Operations.root(a, b)  # We call the root function to find the power of the base to the inverse of exponent
                            except ValueError as e:
                                # This part handles the case where someone tries to raise power by zero or if base is negative, which we can't do.
                                # The root function will throw an error if someone tries raise power by zero or if base is negative, and we catch that error here.
                                print(e)  # Show the error message.
                                continue  # Go back to the top of the loop and try again.
                        elif command.lower() == "modulus":
                            try:
                                result = Operations.modulus(a, b)  # We call the modulus function to divide the two numbers and return the remainder
                            except ValueError as e:
                                # This part handles the case where someone tries to divide by zero, which we can't do.
                                # The modulus function will throw an error if someone tries dividing by zero, and we catch that error here.
                                print(e)  # Show the error message.
                                continue  # Go back to the top of the loop and try again.
                        elif command.lower() == "int_divide":
                            try:
                                result = Operations.integerDivide(a, b)  # We call the integer division function to divide the two numbers.
                            except ValueError as e:
                                # This part handles the case where someone tries to divide by zero, which we can't do.
                                # The integer division function will throw an error if someone tries dividing by zero, and we catch that error here.
                                print(e)  # Show the error message.
                                continue  # Go back to the top of the loop and try again.
                        elif command.lower() == "percent":
                            try:
                                result = Operations.percentage(a, b)  # We call the percentage function to divide the two numbers and mutliply by 100.
                            except ValueError as e:
                                # This part handles the case where someone tries to divide by zero, which we can't do.
                                # The percentage function will throw an error if someone tries dividing by zero, and we catch that error here.
                                print(e)  # Show the error message.
                                continue  # Go back to the top of the loop and try again.
                        elif command.lower() == "abs_diff":
                                result = Operations.absoluteDifference(a, b)  # We call the absolute difference function to subtract the two numbers.
                        else:
                            # If the user types an operation we don't understand, we show them a message.
                            print(f"Unknown operation '{command}'. Supported operations: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
                            continue  # Go back to the top of the loop and try again.

                        print(f"\nResult: {result}")
                    except (ValueError) as e:
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

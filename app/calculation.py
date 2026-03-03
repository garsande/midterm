# calculation.py


# Import ABC (Abstract Base Class) and abstractmethod from Python's abc module.
# Abstract Base Classes (ABCs) allow us to define a contract for our subclasses, specifying 
# methods that they must implement. This helps in establishing a standard interface for 
# similar objects without enforcing specific details on how they should work.
from abc import ABC, abstractmethod

# Import the Operation class from the app.operation module. 
# The Operation class is where our basic mathematical functions (e.g., addition, subtraction) are defined.
# Rather than implementing arithmetic logic within each calculation class, we encapsulate it in a 
# separate class to promote modularity. This makes it easier to modify or extend these functions independently.
from app.operations import Operations

# -----------------------------------------------------------------------------------
# Abstract Base Class: Calculation
# -----------------------------------------------------------------------------------
class Calculation(ABC):
    """
        The Calculation class is an Abstract Base Class (ABC) that defines a blueprint 
        for all mathematical calculations in the calculator program. This class establishes 
        a consistent interface that all calculation types (such as addition, subtraction, etc.) 
        must follow. 
    """
    def __init__(self, a: float, b: float) -> float:
        """
        Initializes a Calculation instance with two operands (numbers involved in the calculation).
        
        **Parameters:**
        - `a (float)`: The first operand.
        - `b (float)`: The second operand.
        """
        self.a: float = a  # Stores the first operand as a floating-point number.
        self.b: float = b  # Stores the second operand as a floating-point number.

    def __str__(self) -> str:
        """
        Provides a user-friendly string representation of the Calculation instance, 
        showing the operation name, operands, and result. This enhances **Readability** 
        and **Debugging** by giving a clear output for each calculation.

        **Returns:**
        - `str`: A string describing the calculation and its result.
        """

        result = self.execute()
        operation_name = self.__class__.__name__.replace('Calculation','')
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"
    
    def __repr__(self) -> str:
        """
        Provides a technical, unambiguous representation of the Calculation instance 
        showing the class name and operand values. This is useful for debugging 
        since it gives a clear and consistent format for all Calculation objects.

        **Returns:**
        - `str`: A string containing the class name and operands.
        """

        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"
    
    @abstractmethod
    def execute(self) -> float:
        """
        Abstract method to perform the calculation. Subclasses will provide specific 
        implementations of this method, defining the arithmetic for each operation.

        **Returns:**
        - `float`: The result of the calculation.
        """
        pass  # The actual implementation will be provided by the subclass. # pragma: no cover


# -----------------------------------------------------------------------------------
# Factory Class: CalculationFactory
# -----------------------------------------------------------------------------------

class CalculationFactory:
    """
    The CalculationFactory is a **Factory Class** responsible for creating instances 
    of Calculation subclasses. This design pattern allows us to encapsulate the 
    logic of object creation and make it flexible.
    """
    # dict object to hold a mapping of calculation types like add or subtract
    _calculations = {}

    @classmethod
    def register_calculation(cls,calculation_type: str):
        """
        This method is a decorator used to register a specific Calculation subclass 
        under a unique calculation type. Registering classes with string identifiers 
        like "add" or "multiply" enables easy access to different operations 
        dynamically at runtime.

        **Parameters:**
        - `calculation_type (str)`: A short identifier for the type of calculation 
          (e.g., 'add' for addition).
        """
        def decorator(subclass):
            calculation_type_lower = calculation_type.lower()
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            cls._calculations[calculation_type_lower] = subclass
            return subclass
        return decorator
    
    @classmethod
    def create_calculation(cls,calculation_type: str, a: float, b: float) -> Calculation:
        """
        Factory method that creates instances of Calculation subclasses based on 
        a specified calculation type.

        **Parameters:**
        - `calculation_type (str)`: The type of calculation ('add', 'subtract', 'multiply', 'divide').
        - `a (float)`: The first operand.
        - `b (float)`: The second operand.
        
        **Returns:**
        - `Calculation`: An instance of the appropriate Calculation subclass.
        """
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)
        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Unsupported calculation type: '{calculation_type}', Available types: {available_types} ")
        return calculation_class(a,b)


# -----------------------------------------------------------------------------------
# Concrete Calculation Classes
# -----------------------------------------------------------------------------------

# Each of these classes defines a specific calculation type (addition, subtraction, 
# multiplication, or division). These classes inherit from Calculation, implementing 
# the `execute` method to perform the specific arithmetic operation. 

@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    """
    AddCalculation represents an addition operation between two numbers.
    
    """

    def execute(self) -> float:
        # Calls the addition method from the Operations module to perform the addition.
        return Operations.addition(self.a, self.b)
    
@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    """
    SubtractCalculation represents an subtraction operation between two numbers.
    
    """

    def execute(self) -> float:
        # Calls the subtraction method from the Operations module to perform the subtraction.
        return Operations.subtraction(self.a, self.b)
    
@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    """
    MultiplyCalculation represents a multiplication operation between two numbers.
    
    """

    def execute(self) -> float:
        # Calls the multiply method from the Operations module to perform the multiplication.
        return Operations.multiplication(self.a, self.b)
    

@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    """
    DivideCalculation represents a division operation between two numbers.
    
    """

    def execute(self) -> float:
        # check if b is zero
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        # Calls the divide method from the Operations module to perform the division.
        return Operations.division(self.a, self.b)

@CalculationFactory.register_calculation('power')
class PowerCalculation(Calculation):
    """
    PowerCalculation represents a power operation between two numbers.
    
    """

    def execute(self) -> float:
         # check if b is zero
        if self.b < 0:
            raise ValueError("Cannot calculate power for negative number")
        # Calls the power method from the Operations module to calculate the power of base to exponent.
        return Operations.power(self.a, self.b)

@CalculationFactory.register_calculation('root')
class RootCalculation(Calculation):
    """
    RootCalculation represents a root operation between two numbers.
    
    """

    def execute(self) -> float:
        if self.a < 0:
            raise ValueError("Cannot calculate root of negative number")
        if self.b == 0:
            raise ZeroDivisionError("Zero root is undefined")
        # Calls the root method from the Operations module to calculate the root of base to exponent
        return Operations.root(self.a, self.b)

@CalculationFactory.register_calculation('abs_diff')
class AbsoluteDifferenceCalculation(Calculation):
    """
    AbsoluteDifferenceCalculation represents an subtraction operation between two numbers.
    
    """

    def execute(self) -> float:
        # Calls the subtraction method from the Operations module to perform the subtraction with positive result.
        return Operations.absoluteDifference(self.a, self.b)
    
@CalculationFactory.register_calculation('int_divide')
class IntegerDivideCalculation(Calculation):
    """
    IntegerDivideCalculation represents a division operation between two numbers.
    
    """

    def execute(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        # Calls the division method from the Operations module to perform the division and provide Integer result
        return Operations.integerDivide(self.a, self.b)
    
@CalculationFactory.register_calculation('modulus')
class ModulusCalculation(Calculation):
    """
    ModulusCalculation represents a modulus operation between two numbers.
    
    """

    def execute(self) -> float:
        if self.b ==0:
            raise ZeroDivisionError("Cannot find modulus if divisor is zero")
        # Calls the modulus method from the Operations module to perform the division and provide the remainder.
        return Operations.modulus(self.a, self.b)
    
@CalculationFactory.register_calculation('percent')
class PercentageCalculation(Calculation):
    """
    PercentageCalculation represents a percent operation between two numbers.
    
    """

    def execute(self) -> float:
        if self.b ==0:
            raise ZeroDivisionError("Cannot find percentage for zero")
        # Calls the percent method from the Operations module to calculate the percentage.
        return Operations.percentage(self.a, self.b)
    

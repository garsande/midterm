## Operations.py ##

from decimal import Decimal

class Operations:
    """
        Starting with the basic Operation class which encapsulates basic arithmetic operations as static methods.
        Eventually planning to change this class to use Factory pattern to create operations. them to 
        
    """

    @staticmethod  
    def addition(a:Decimal, b:Decimal) -> Decimal:
        """
        Adds two numbers and returns the result.

        **Parameters:**
        - a (Decimal): The first number to add.
        - b (Decimal): The second number to add.
        
        **Returns:**
        - Decimal: The sum of a and b.

        **Example:**
        >>> Operation.addition(5.0, 3.0)
        8.0
        """
        return a + b  # Add two numbers and returns the result.
    
    @staticmethod  
    def subtraction(a:Decimal, b:Decimal) -> Decimal:
        """
        Subtracts the second number from the first and returns the result.

        **Parameters:**
        - a (Decimal): The number from which to subtract.
        - b (Decimal): The number to subtract.
        
        **Returns:**
        - Decimal: The difference between a and b.

        **Example:**
        >>> Operation.subtraction(10.0, 4.0)
        6.0
        """
        return a - b  # Subtract two numbers and returns the result.
    
    @staticmethod
    def multiplication(a: Decimal, b: Decimal) -> Decimal:
        """
        Multiplies two numbers and returns the product.

        **Parameters:**
        - a (Decimal): The first number to multiply.
        - b (Decimal): The second number to multiply.
        
        **Returns:**
        - Decimal: The product of a and b.

        **Example:**
        >>> Operation.multiplication(2.0, 3.0)
        6.0

        """
        return a * b  # Multiplies the two numbers and returns the product.
    
    @staticmethod
    def division(a: Decimal, b: Decimal) -> Decimal:
        """
        Divides the first number by the second and returns the quotient.

        **Parameters:**
        - a (Decimal): The dividend.
        - b (Decimal): The divisor.
        
        **Returns:**
        - Decimal: The quotient of a divided by b.

        **Raises:**
        - ValueError: If the divisor b is zero, as division by zero is undefined.

        **Example:**
        >>> Operation.division(10.0, 2.0)
        5.0
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")  # Raises an error if division by zero is attempted.
        return a / b  # Divides a by b and returns the quotient.
    
    @staticmethod
    def power(a: Decimal, b: Decimal) -> Decimal:
        """
        Takes two numbers and returns the power of the base raised to exponent.

        **Parameters:**
        - a (Decimal): The base number.
        - b (Decimal): The exponent.
        
        **Returns:**
        - Decimal: The base  a raised to the exponent of b.

        **Example:**
        >>> Operation.power(2.0, 3.0)
        8.0
        Raises:
            ValueError: If the exponent is negative.
        """
        if b < 0:
            raise ValueError("Negative exponents not supported")
        return Decimal(pow(Decimal(a), Decimal(b)))  # Returns the power of the base to exponent.

    @staticmethod
    def root(a: Decimal, b: Decimal) -> Decimal:
        """
        Takes two parameters and return the nth root of other number

        **Parameters:**
        - a (Decimal): Number from which the root is taken.
        - b (Decimal): Degree of the root.

        **Returns:**
        - Decimal: The base a raised to the inverse power of b.

        **Example:**
        >>> Operation.root(4.0, 2.0)
        2.0
         
        Raises:
            ValueError: If the number is negative or the root degree is zero.
        """
        if a < 0:
            raise ValueError("Cannot calculate root of negative number")
        if b == 0:
            raise ValueError("Zero root is undefined")
        return Decimal(pow(Decimal(a), 1 / Decimal(b))) # Returns the power of the base to the inverse of exponent
    
    @staticmethod
    def modulus(a: Decimal, b: Decimal) -> Decimal:
        """
        Divides the first number by the second and returns the remainder.

        **Parameters:**
        - a (Decimal): The dividend.
        - b (Decimal): The divisor.
        
        **Returns:**
        - Decimal: The remainder of a divided by b.

        **Raises:**
        - ValueError: If the divisor b is zero, as division by zero is undefined.

        **Example:**
        >>> Operation.modulus(10.0, 3.0)
        1.0
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")  # Raises an error if division by zero is attempted.
        return a % b  # Divides a by b and returns the remainder.
    
    @staticmethod
    def integerDivide(a: Decimal, b: Decimal) -> Decimal:
        """
        Divides the first number by the second and returns the integer quotient.

        **Parameters:**
        - a (Decimal): The dividend.
        - b (Decimal): The divisor.
        
        **Returns:**
        - Decimal: The integer quotient of a divided by b.

        **Raises:**
        - ValueError: If the divisor b is zero, as division by zero is undefined.

        **Example:**
        >>> Operation.int_divide(10.0, 3.0)
        1.0
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")  # Raises an error if division by zero is attempted.
        return a // b  # Divides a by b and returns the integer quotient.
    
    @staticmethod  
    def absoluteDifference(a:Decimal, b:Decimal) -> Decimal:
        """
        Subtracts the second number from the first and returns the absolute value of result.

        **Parameters:**
        - a (Decimal): The number from which to subtract.
        - b (Decimal): The number to subtract.
        
        **Returns:**
        - Decimal: The difference between a and b as a positive integer.

        **Example:**
        >>> Operation.abs_diff(10.0, 14.0)
        4.0
        """
        return abs(a - b)  # Subtract two numbers and returns the absolute value of result.
    
    @staticmethod
    def percentage(a: Decimal, b: Decimal) -> Decimal:
        """
        Divides the first number by the second and then multiply by 100 to get percentage value

        **Parameters:**
        - a (Decimal): The dividend.
        - b (Decimal): The divisor.
        
        **Returns:**
        - Decimal: The percent value of a divided by b and multiplied by 100.

        **Raises:**
        - ValueError: If the divisor b is zero, as division by zero is undefined.

        **Example:**
        >>> Operation.percent(10.0, 45.6)
        4.56
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")  # Raises an error if division by zero is attempted.
        return (a / b) * 100  # Divides a by b and then multiplies by 100 to get percentage value.
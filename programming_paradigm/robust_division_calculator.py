def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)

        # check if denominator is zero
        if denominator == 0:
            raise ZeroDivisionError
        
        # Perform operation
        result = numerator/denominator
        return f"The result of the division is {result}"

    except ValueError as ve:
        return f"Error: Please enter numeric values only."

    except ZeroDivisionError as zde:
        return f"Error: Cannot divide by zero."

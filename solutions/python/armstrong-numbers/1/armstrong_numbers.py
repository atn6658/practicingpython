def is_armstrong_number(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")

    num_digits = len(str(number))
    digits = [int(d) for d in str(number)]
    powered_digits = [d ** num_digits for d in digits]
    total = sum(powered_digits)

    if total == number:
        return True
    else:
        return False

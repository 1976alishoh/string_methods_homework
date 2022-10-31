def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s.isdigit():
        return True
    else:
        return False
print(main("12345"))
print(main("2022ABC"))
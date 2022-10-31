def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s.islower():
        return True
    else:
        return False

print(main("codeschool"))
print(main("Mobile"))
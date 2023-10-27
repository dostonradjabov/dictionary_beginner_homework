def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    a = []
    for i in data:
        a.append(i)
    return max(a)
print(find_max_value(data={
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  }
))
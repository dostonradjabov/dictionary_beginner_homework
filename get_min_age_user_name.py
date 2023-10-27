def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    mn = 10000
    mx = 0
    for i in data:
        if i["age"]<mn:
            mn = i["age"]
            mx = i["name"]
    return mx
print(get_min_age_user_name(data=[
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
  ]))

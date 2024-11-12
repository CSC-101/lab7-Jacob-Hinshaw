from typing import Optional

# this function takes an input and if it can be converted to a float, it is. Otherwise, none is returned.
def str_to_float(input1) -> Optional[float]:
    try:
        return float(input1)
    except ValueError:
        return None


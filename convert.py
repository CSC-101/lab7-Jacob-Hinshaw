from typing import Optional


def str_to_float(input1) -> Optional[float]:
    try:
        return float(input1)
    except ValueError:
        return None


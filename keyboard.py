from typing import Optional

import convert


# this function takes any input from the user and if it is a float, appends it to a list and returns the list
# when the user inputs "done"
def gather_numbers() -> list[float]:
    output_list = []
    while True:
        input1 = input("number?")
        if input1 == "done":
            return output_list
        output_list.append(convert.str_to_float(input1))




if __name__ == '__main__':
    print(gather_numbers())
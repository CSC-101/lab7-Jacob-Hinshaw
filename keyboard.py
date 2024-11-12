from typing import Optional

import convert

if __name__ == '__main__':



    def gather_numbers():
        output_list = []
        while True:
            input1 = input("number?")
            if input1 == "done":
                return output_list
            output_list.append(convert.str_to_float(input1))


print(gather_numbers())
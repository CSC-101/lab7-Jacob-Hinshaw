import sys
import keyboard

if __name__ == '__main__':
    print(sys.argv)

# This function takes arguments from the command line and sums all the integers or float values
def add():
    total = 0
    for num in sys.argv:
        try:
            total += float(num)
        except ValueError:
            continue
    return total

print(add())




from calculator import add, subtract
from string_utils import reverse_string
from list_processor import sum_list

def main():
    print("Calculator:")
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))

    print("\nString Utils:")
    print('Reverse "hello":', reverse_string("hello"))

    print("\nList Processor:")
    print("Sum of [1, 2, 3]:", sum_list([1, 2, 3]))

if __name__ == "__main__":
    main()

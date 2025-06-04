"""main pfile for finding unique pairs with equal sums."""

from utils import print_equal_sums, get_unique_pairs
from models import CArray


if __name__ == "__main__":
    # array: str = '{6, 4, 12, 10, 22, 54, 32, 42, 21, 11}'
    # array: str = '{1, 1, 1, 1, 1, 12, 86}'
    array: str = input('Enter array, e.g., {1, 2, 3}: ')
    li: list = CArray(array).to_list()
    if not li:
        print("Array is empty or invalid.")
    else:
        dict_to_print: dict = get_unique_pairs(li)
        print_equal_sums(dict_to_print)

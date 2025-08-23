
from typing import List, Tuple


def process_list_operations() -> Tuple[List[int], int]:
    """
    Perform a sequence of operations on a list.

    Steps:
    1. Create an empty list.
    2. Append 10, 20, 30, and 40 to the list.
    3. Insert 15 at the second position.
    4. Extend the list with [50, 60, 70].
    5. Remove the last element.
    6. Sort the list in ascending order.
    7. Find and return the index of 30.

    Returns:
        Tuple[List[int], int]: The final list and the index of 30.
    """
    # Step 1: Create an empty list
    my_list: List[int] = []

    # Step 2: Append elements to the list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    # Step 3: Insert value 15 at the second position (index 1)
    my_list.insert(1, 15)

    # Step 4: Extend the list with additional elements
    my_list.extend([50, 60, 70])

    # Step 5: Remove the last element
    my_list.pop()

    # Step 6: Sort the list in ascending order
    my_list.sort()

    # Step 7: Find the index of the value 30
    index_of_30 = my_list.index(30)

    return my_list, index_of_30


def main() -> None:
    """
    Entry point for running the list operations as a script.
    Prints the final list and the index of 30.
    """
    final_list, index_of_30 = process_list_operations()

    print("Index of 30 in my_list:", index_of_30)
    print("Final list:", final_list)


if __name__ == "__main__":
    main()

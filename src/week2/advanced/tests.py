
import pytest
from list import process_list_operations


def test_process_list_operations():
    """
    Test the process_list_operations function to ensure it performs
    all list operations correctly and returns the expected results.
    """
    # Execute the function
    final_list, index_of_30 = process_list_operations()

    # Step 1: Ensure the final list is sorted
    assert final_list == sorted(
        final_list), "List should be sorted in ascending order."

    # Step 2: Ensure the value 15 is present at the correct position
    assert 15 in final_list, "Value 15 should be present in the list."

    # Step 3: Ensure the index of 30 is correct
    assert final_list[index_of_30] == 30, "Index returned should point to value 30."

    # Step 4: Ensure the list contains all expected values except 70
    expected_values = [10, 15, 20, 30, 40, 50, 60]
    assert final_list == expected_values, f"List should be {expected_values}."

    # Step 5: Ensure 70 is not in the list
    assert 70 not in final_list, "Value 70 should have been removed from the list."


if __name__ == "__main__":
    pytest.main([__file__])

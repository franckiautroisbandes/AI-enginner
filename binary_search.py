def binary_search_iterative(sorted_list, target):
    """Return the index of target in sorted_list, or -1 if not found."""
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == target:
            return mid

        elif sorted_list[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def binary_search_recursive(sorted_list, target, low=0, high=None):
    """Return the index of target in sorted_list, or -1 if not found."""

    if high is None:
        high = len(sorted_list) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if sorted_list[mid] == target:
        return mid

    elif sorted_list[mid] < target:
        return binary_search_recursive(
            sorted_list, target, mid + 1, high
        )

    else:
        return binary_search_recursive(
            sorted_list, target, low, mid - 1
        )


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]

    print(binary_search_iterative(numbers, 9))
    print(binary_search_recursive(numbers, 5))
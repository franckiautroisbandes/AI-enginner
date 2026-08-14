import random
import time


def two_sum_brute(numbers, target):
    """Return True if any two different numbers sum to target.

    Uses a brute-force approach with O(n²) time complexity.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True

    return False


def two_sum_set(numbers, target):
    """Return True if any two numbers sum to target.

    Uses a set to achieve O(n) average time complexity.
    """
    seen = set()

    for number in numbers:
        complement = target - number

        if complement in seen:
            return True

        seen.add(number)

    return False


if __name__ == "__main__":
    # Create 10,000 random integers
    random.seed(42)
    numbers = [random.randint(-100_000, 100_000) for _ in range(10_000)]

    target = 12_345

    # Time brute-force version
    start = time.perf_counter()
    brute_result = two_sum_brute(numbers, target)
    brute_time = time.perf_counter() - start

    # Time set version
    start = time.perf_counter()
    set_result = two_sum_set(numbers, target)
    set_time = time.perf_counter() - start

    print("Brute force:")
    print("Result:", brute_result)
    print("Time:", brute_time, "seconds")

    print("\nSet:")
    print("Result:", set_result)
    print("Time:", set_time, "seconds")
import random

def get_evens(numbers):
    """Return only the even numbers from the list, in original order."""
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

def bubble_sort_descending(numbers):
    """Return a new list sorted descending, implemented manually (no sorted())."""
    # Create a copy so we do not modify the original list
    arr = list(numbers)
    n = len(arr)
    
    # Manual Bubble Sort in descending order (< flips the order)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                # Pythonic swap (cleaner than using a temp variable)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def second_largest(numbers):
    """Return the second-largest value without sorting the list."""
    if len(numbers) < 2:
        return None
        
    largest = float('-inf')
    second = float('-inf')
    
    # O(n) Single-pass search tracking the two highest values
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
            
    return second if second != float('-inf') else None

if __name__ == "__main__":
    # Generate the random dataset
    random_list = [random.randint(1, 101) for _ in range(20)]
    
    print("Original:", random_list)
    print("Evens:", get_evens(random_list))
    print("Descending:", bubble_sort_descending(random_list))
    print("Second largest:", second_largest(random_list))
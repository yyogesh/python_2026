def manual_stats(numbers):
    """
    Returns (sum, min, max) without using built-in sum/min/max.
    """
    if not numbers:
        return 0, 0, 0
    total = 0
    min_val = max_val = numbers[0]
    for item in numbers:
        total  += item
        if item < min_val:# 3 # -1
            min_val = item
        if max_val < item:
            max_val = item

    return total, min_val, max_val


if __name__ == "__main__":
    # Sample list of 10 numbers
    sample = [3, -1, 7, 2, -5, 8, 3, 2, 9, -2]
    print("Original list:", sample)


    total, mn, mx = manual_stats(sample)
    print(f"\n1. Sum = {total}, Min = {mn}, Max = {mx}")
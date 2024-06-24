def print_positive_numbers(start, end):
    for num in range(start, end + 1):
        if num > 0:
            print(num)

# Example usage:
start_range = -5
end_range = 10

print(f"Positive numbers between {start_range} and {end_range}:")
print_positive_numbers(start_range, end_range)

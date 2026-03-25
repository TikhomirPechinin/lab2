def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)  # Деление, которого может не быть

nums = [10, 20, 30]
print(calculate_average(nums))
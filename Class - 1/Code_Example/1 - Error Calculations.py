true_value = float(input("Enter the true value: "))
approx_value = float(input("Enter the approximate value: "))

# Absolute Error
absolute_error = abs(true_value - approx_value)

# Relative Error
relative_error = absolute_error / abs(true_value)

# Percentage Error
percentage_error = relative_error * 100

print(f"Absolute Error: {absolute_error}")
print(f"Relative Error: {relative_error}")
print(f"Percentage Error: {percentage_error}%")
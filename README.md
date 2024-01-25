def convert_to_indian_currency(number):: This line defines a function named
number_str = str(number): Converts the input integer to a string so that we can process each digit individually.
if len(number_str) > 3:: Checks if the length of the string representation of the number is greater than 3
Inside the if block:

last_three_digits = number_str[-3:]: Extracts the last three digits of the number.
remaining_digits = number_str[:-3]: Extracts the remaining digits of the number (excluding the last three).
if remaining_digits:: Checks if there are any remaining digits after extracting the last three digits.

Inside the if block:

remaining_digits = convert_to_indian_currency(int(remaining_digits)): Calls the convert_to_indian_currency function recursively to convert the remaining digits.
Returns the result of the recursion, concatenated with a comma and the last three digits. This ensures the proper grouping of digits in the Indian currency format.
else:: If there are no remaining digits, returns just the last three digits.

else: (outside the first if block): If the number has three or fewer digits, directly returns the string representation of the number.

Example usage:

amount = 123456789: Sets an example amount.
indian_currency = "₹" + convert_to_indian_currency(amount): Calls the function to convert the amount to Indian currency notation and adds the Indian Rupee symbol.
print(indian_currency): Prints the result.

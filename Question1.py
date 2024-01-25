def convert_to_indian_currency(number):
    number_str = str(number)

    if len(number_str) > 3:
        last_three_digits = number_str[-3:]
        remaining_digits = number_str[:-3]

        if remaining_digits:
            remaining_digits = convert_to_indian_currency(int(remaining_digits))
            return remaining_digits + "," + last_three_digits
        else:
            return last_three_digits
    else:
        return number_str

# Example usage:
amount = 123456789
indian_currency = "₹" + convert_to_indian_currency(amount)
print(indian_currency)

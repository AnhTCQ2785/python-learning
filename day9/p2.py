def validate_credit_card(card_number):

    card_number = card_number.strip().replace(" ", "")


    if not card_number.isdigit():
        return False


    digits = [int(digit) for digit in card_number]


    reversed_digits = digits[::-1]


    total_sum = 0
    for index, digit in enumerate(reversed_digits):
        if index % 2 == 1:
            doubled_digit = digit * 2
            if doubled_digit > 9:
                doubled_digit -= 9
            total_sum += doubled_digit
        else:
            total_sum += digit


    if total_sum % 10 == 0:
        return True
    else:
        return False



if __name__ == "__main__":

    card_number = input("Enter your credit card number: ")

   
    if validate_credit_card(card_number):
        print("The credit card number is valid.")
    else:
        print("The credit card number is not valid.")

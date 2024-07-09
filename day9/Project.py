def validate_credit_card(card_number):

    card_number = card_number.replace(" ", "")
    digits = list(map(int, card_number))


    reversed_digits = digits[::-1]


    total_sum = 0
    for i, digit in enumerate(reversed_digits):
        if i % 2 == 1:
            doubled_digit = digit * 2
            if doubled_digit > 9:
                doubled_digit -= 9
            total_sum += doubled_digit
        else:
            total_sum += digit


    return total_sum % 10 == 0



test_card_numbers = [
    "1234567898765432",
    "1234567898765431",
    "378282246310005",
    "371449635398431"
]


for card_number in test_card_numbers:
    if validate_credit_card(card_number):
        print(f"Số thẻ {card_number} là hợp lệ.")
    else:
        print(f"Số thẻ {card_number} không hợp lệ.")

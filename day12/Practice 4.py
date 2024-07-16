def is_palindrome(word):
    cleaned_word = word.strip().lower().replace(" ", "")
    reversed_word = cleaned_word[::-1]
    if cleaned_word == reversed_word:
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

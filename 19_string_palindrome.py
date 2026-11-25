
def is_palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"


word = "Madam"

print(is_palindrome(word))

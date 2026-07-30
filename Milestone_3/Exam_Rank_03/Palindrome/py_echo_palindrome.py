def echo_validator(text: str) -> bool:
    if not text:
        return False

    clean_text = "".join(text.split()).lower()

    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    tests = [
        ("racecar", True),
        ("A man a plan a canal Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw", True),
        ("hello", False),
        ("Madam Im Adam", True),
        ("", False),
        ("a", True),
        ("ab", False),
    ]

    for row in tests:
        print(echo_validator(row[0]) == row[1])
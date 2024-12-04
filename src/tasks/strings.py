import re

def reverse_string(string):
    return string[::-1]


def word_count(text):
    """Count the number of words in the text."""
    words = re.findall(r'\b\w+\b', text)  # This will split by word boundaries and ignore punctuation
    return len(words)

def pattern_match(text, pattern):
    """Check if the pattern exists in the text (case insensitive)."""
    print(f"Checking if '{pattern}' is in '{text}'")  # Debugging line
    return pattern.lower() in text.lower()


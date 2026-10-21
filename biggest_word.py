# 7 - 7 - 2026

import string

# Step 1: Get the input from the user
paragraph = input("Enter a paragraph:")

# Step 2: Split the paragraph into words and remove puncuation
# We'll use string.puncuation to remove puncuation marks
words = paragraph.split()

# Remove puncuation from each word and check for the longest word
longet_word = ""
max_length = 0

for word in words:
    # Remove punctuation and check the length of the word
    cleaned_word = word.strip(string.punctuation)

    # If the length of cleaned word is greater than the current max_length, update
    if len(cleaned_word) > max_length:
        longest_word = cleaned_word
        max_length = len(cleaned_word)

# Step 3: Output the results
print(f"The biggest word is '{longest_word}' with '{max_length}' letters.")
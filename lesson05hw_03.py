"""
Program to convert user input into a hashtag.
"""

user_input = input("Enter a text: ")

# Capitalize each word and join them into a single string
hashtag = "".join(word.capitalize() for word in user_input.split())

# Remove punctuation and spaces
clean_hashtag = "".join(char for char in hashtag if char.isalnum())

# Truncate to 140 characters if needed
clean_hashtag = clean_hashtag[:139] if len(clean_hashtag) > 139 else clean_hashtag

print(f"Hashtag: #{clean_hashtag}")

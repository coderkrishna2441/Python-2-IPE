# 1. Email Validatior: 
# Create a program that validates email addresses using regex. 
# It should check if an input string is a valid email address according to common email address rules.
# The regex pattern should be common one for basic email address validation. 
# It checks for the following:-
# Starts with one or more alphanumeric characters, dots, underscores, percentage signs, plus signs, or hyphens.
# Followed by the "@" symbol.
# Followed by one or more alphanumeric characters or hyphens.
# Followed by a dot (.) and at least two or more alphabetic characters.

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Example usage:
email = "your_email@example.com"
if validate_email(email):
  print("Valid email address")
else:
  print("Invalid email address")


# 2. Password Strength Checker
# Create a program that checks the strength of a password using regex. 
# The program should ensure the password meets certain criteria,such as containing 
# at least one uppercase letter, 
# one lowercase letter,
# one digit,
# one special character

def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[\w\d@#$!%*?&]{8,}$"
    # The question mark makes the preceding element optional, It matches zero or one occurrence.
    # The equal sign is used when, following pattern must match,but the pattern is excluded.
    return re.match(pattern, password) is not None

# Example usage:
password = "MyStrongPassword123!"
if validate_password(password):
  print("Strong password")
else:
  print("Weak password")



# 3. Phone Number 
# Create a program that extracts phone numbers from a text using regex. 
# It should find and display all valid phone numbers in the input text.
# The regex pattern should account for various formats, including: 
# +91 1234567890 
# 9876543210 
# 080-12345678 
# +91-9876543210


def extract_phone_numbers(text):
  pattern = r"(\+91|0)?\s?\d{10}"
  matches = re.findall(pattern, text)
  return matches

# Example usage:
text = "My phone number is +91 1234567890. You can also call me at 9876543210 or 080-12345678."
phone_numbers = extract_phone_numbers(text)
print(phone_numbers)
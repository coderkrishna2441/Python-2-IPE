# 1. URL Extractor
# Create a program that extracts URLs from a text using regex. 
# It should find and display all valid URLs in the input text.
# Example  of URL : www.google.com

import re

def extract_urls(text):

  # Improved regex pattern for various URL formats:
  pattern = r"(?i)\b((https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?\']))"
  matches = re.findall(pattern, text)
  return matches

# Example usage:
text = "Visit us at www.google.com or check out our new blog post at https://blog.example.com/latest-news"
urls = extract_urls(text)
print(urls)


# 2. IP Validator
# Create a program that validates IP addresses using regex. 
# It should check if an input string is a valid IPv4 address or not.
# Example  of IPv4 address :192.0.2.146

def validate_ipv4_address(address):
  
  pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
  return re.match(pattern, address) is not None

# Example usage:
ip_address = "192.0.2.146"
if validate_ipv4_address(ip_address):
  print("Valid IPv4 address")
else:
  print("Invalid IPv4 address")


# 3. HTML Tag Extractor
# Create a program that extracts HTML tags from an HTML document using regex. 
# It should find and display all HTML tags in the input text.

import re

def extract_html_tags(html_text):

  pattern = r"<[^>]*>"
  tags = re.findall(pattern, html_text)
  return tags

# Example usage:
html_text = "<html><head><title>Example Page</title></head><body><h1>Hello, world!</h1><p>This is a paragraph.</p></body></html>"
tags = extract_html_tags(html_text)
print(tags)
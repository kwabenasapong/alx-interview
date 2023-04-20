#!/usr/bin/env python3
"""
testing driving utf-8 encoding and decoding
"""

# Create a Unicode string
unicode_string = "A"

# Encode the string as UTF-8 bytes
utf8_bytes = unicode_string.encode('utf-8')

# Print the UTF-8 bytes
print("utf-8 bytes:", utf8_bytes)

# Decode the UTF-8 bytes back into a Unicode string
decoded_string = utf8_bytes.decode('utf-8')

# Print the original string and the decoded string to verify they are the same
print("Original string:", unicode_string)
print("Decoded string:", decoded_string)

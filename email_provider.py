"""
Parses the email provider from an email address.

Since:
    1.0.0

Category:
    Parsing

Args:
    param1 (str) email_address: The email address to be parsed.

Returns:
    string: The provider from the email address.

Example:
    >>> print(email_provider('john.smith@gmail.com'))
    gmail.com
"""


def email_provider(email_address):
    # Find the @ for slice starting point
    start_point = email_address.find('@') + 1
    # Slice the provider from the email address
    provider = email_address[start_point:]
    return provider
